import React from 'react';
import { Table } from 'antd';
import { getPendingTransactions } from '../../api/pendingTransactions';
import { IPendingTransactions } from '../../models/IPendingTransactions';
import { EXPLORER_TX_SEARCH_URL } from '../../constants';
import { ITransactionWithFeePerByte } from '../../models/ITransaction';
import { SortOrder } from 'antd/lib/table/interface';
import { ITableFilter } from '../../models/ITableFilter';

const PendingTransactions = () => {
    const [pendingTransactions, setPendingTransactions] = React.useState<Array<ITransactionWithFeePerByte> | []>([]);
    const [txIdFilters, setTxIdFilters] = React.useState<Array<ITableFilter> | []>([]);
    const [sourceAddressFilters, setSourceAddressFilters] = React.useState<Array<ITableFilter> | []>([]);
    const [isLoading, setLoading] = React.useState<boolean>(true);

    React.useEffect(() => {
        setLoading(true);
        getPendingTransactions().then((pendingTransactionsResponse: IPendingTransactions) => {
            setPendingTransactions(
                pendingTransactionsResponse.transactions.map(
                    (transaction) =>
                        ({
                            ...transaction,
                            feePerByte: transaction.transactionFee / transaction.size
                        } as ITransactionWithFeePerByte)
                )
            );
            setTxIdFilters(
                pendingTransactionsResponse.transactions.map((transaction) => ({
                    text: transaction.txId,
                    value: transaction.txId
                }))
            );
            setSourceAddressFilters(
                pendingTransactionsResponse.transactions.map((transaction) => ({
                    text: transaction.sourceAddress,
                    value: transaction.sourceAddress
                }))
            );

            setLoading(false);
        });
    }, []);

    const columns = [
        {
            title: 'Transaction ID',
            dataIndex: 'txId',
            key: 'txId',
            filters: txIdFilters,
            onFilter: (value: string | number | boolean, record: ITransactionWithFeePerByte) =>
                record.txId.startsWith(value as string),
            filterSearch: true,
            render: (txId: string) => (
                <a href={`${EXPLORER_TX_SEARCH_URL}${txId}`} target="_blank">
                    {`${txId.slice(0, 5)}...${txId.slice(txId.length - 5)}`}
                </a>
            )
        },
        {
            title: 'Source Address',
            dataIndex: 'sourceAddress',
            key: 'sourceAddress',
            filters: sourceAddressFilters,
            onFilter: (value: string | number | boolean, record: ITransactionWithFeePerByte) =>
                record.sourceAddress.startsWith(value as string),
            filterSearch: true
        },
        {
            title: 'Fee per byte',
            dataIndex: 'feePerByte',
            key: 'feePerByte',
            sortDirections: ['descend', 'ascend'] as Array<SortOrder>,
            defaultSortOrder: 'descend' as SortOrder,
            sorter: (a: ITransactionWithFeePerByte, b: ITransactionWithFeePerByte) => a.feePerByte - b.feePerByte,
            render: (feePerByte: number) => feePerByte.toFixed(8)
        },
        {
            title: 'Fee',
            dataIndex: 'transactionFee',
            key: 'transactionFee',
            sortDirections: ['descend', 'ascend'] as Array<SortOrder>,
            sorter: (a: ITransactionWithFeePerByte, b: ITransactionWithFeePerByte) =>
                a.transactionFee - b.transactionFee
        },
        {
            title: 'Size',
            dataIndex: 'size',
            key: 'size',
            sortDirections: ['descend', 'ascend'] as Array<SortOrder>,
            sorter: (a: ITransactionWithFeePerByte, b: ITransactionWithFeePerByte) => a.size - b.size
        }
    ];

    return <Table loading={isLoading} columns={columns} dataSource={pendingTransactions} />;
};

export default PendingTransactions;
