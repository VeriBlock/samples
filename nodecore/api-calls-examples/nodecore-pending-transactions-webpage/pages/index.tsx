import { Alert, Table } from 'antd';
import { SortOrder } from 'antd/lib/table/interface';
import { ITransactionWithFeePerByteAndGmtDate } from 'models/ITransaction';
import moment from 'moment';
import React from 'react';
import { EXPLORER_TX_SEARCH_URL } from 'utils/constants';

import type { NextPage } from "next";
import { IPendingTransactionsPage } from 'models/pageProps/IPendingTransactionsPage';
import useSWR from 'swr';
import { fetcher } from './api/utils';


const PendingTransactionsPage: NextPage = () => {
  const { data } = useSWR<IPendingTransactionsPage>('/api/pendingTransactions', fetcher, {
    // revalidate the data per second
    refreshInterval: 1000
  });

  const columns = [
    {
      title: "Transaction ID",
      dataIndex: "txId",
      key: "txId",
      filters: data?.txIdFilters,
      onFilter: (
        value: string | number | boolean,
        record: ITransactionWithFeePerByteAndGmtDate
      ) => record.txId.startsWith(value as string),
      filterSearch: true,
      render: (txId: string) => (
        <a
          href={`${EXPLORER_TX_SEARCH_URL}${txId}`}
          target="_blank"
          rel="noreferrer"
        >
          {`${txId.slice(0, 5)}...${txId.slice(txId.length - 5)}`}
        </a>
      ),
    },
    {
      title: "Source Address",
      dataIndex: "sourceAddress",
      key: "sourceAddress",
      filters: data?.sourceAddressFilters,
      onFilter: (
        value: string | number | boolean,
        record: ITransactionWithFeePerByteAndGmtDate
      ) => record.sourceAddress.startsWith(value as string),
      filterSearch: true,
    },
    {
      title: "Fee per byte",
      dataIndex: "feePerByte",
      key: "feePerByte",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      defaultSortOrder: "descend" as SortOrder,
      sorter: (a: ITransactionWithFeePerByteAndGmtDate, b: ITransactionWithFeePerByteAndGmtDate) =>
        a.feePerByte - b.feePerByte,
      render: (feePerByte: number) => feePerByte.toFixed(8),
    },
    {
      title: "Fee",
      dataIndex: "transactionFee",
      key: "transactionFee",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      sorter: (a: ITransactionWithFeePerByteAndGmtDate, b: ITransactionWithFeePerByteAndGmtDate) =>
        a.transactionFee - b.transactionFee,
    },
    {
      title: "Size",
      dataIndex: "size",
      key: "size",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      sorter: (a: ITransactionWithFeePerByteAndGmtDate, b: ITransactionWithFeePerByteAndGmtDate) =>
        a.size - b.size,
    },
    {
      title: "Date (GMT)",
      dataIndex: "gmtDate",
      key: "gmtDate",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      sorter: (a: ITransactionWithFeePerByteAndGmtDate, b: ITransactionWithFeePerByteAndGmtDate) =>
        moment(a.gmtDate).unix() - moment(b.gmtDate).unix(),
    },
  ];
  
  return (
    <section>
      {data?.hasError && (<Alert message={data?.errorMsg} type="error" />)}
      <Table
        loading={data?.isLoading}
        columns={columns}
        pagination={{
          defaultPageSize: 30,
          pageSizeOptions: ['10', '20', '30', '50', '100', `${data ? data.pendingTransactions : 0}`],
          showSizeChanger: true,
          position: ["topRight", "bottomRight"]
        }}
        dataSource={data?.pendingTransactions}
        rowKey="txId"
      />
      <div>Last Update: {(new Date()).toUTCString()}</div>
    </section>
  );
};

export default PendingTransactionsPage;
