import { API_PATH } from 'utils/constants';
import { IPendingTransactions } from 'models/IPendingTransactions';
import { IFailureResponse } from 'models/IFailureResponse';
import { ITransactionWithFeePerByteAndGmtDate } from 'models/ITransaction';
import { NextApiRequest, NextApiResponse } from 'next';
import { request } from 'pages/api/utils';

const getPendingTransactions = async (): Promise<IPendingTransactions> => (
    await request<IPendingTransactions>(
        API_PATH.PENDING_TRANSACTIONS
    )
);

export const fetchPendingTransactions = async () => {
    try {
        const pendingTransactionsResponse: IPendingTransactions =
            await getPendingTransactions();

        return {
            pendingTransactions: (
                pendingTransactionsResponse as IPendingTransactions
            ).transactions.map(
                (transaction) =>
                ({
                    ...transaction,
                    feePerByte: transaction.transactionFee / transaction.size,
                    gmtDate: (new Date(transaction.timestamp * 1000)).toUTCString()
                } as ITransactionWithFeePerByteAndGmtDate)
            ),
            txIdFilters: (
                pendingTransactionsResponse as IPendingTransactions
            ).transactions.map((transaction) => ({
                text: transaction.txId,
                value: transaction.txId,
            })),
            sourceAddressFilters: (
                pendingTransactionsResponse as IPendingTransactions
            ).transactions.map((transaction) => ({
                text: transaction.sourceAddress,
                value: transaction.sourceAddress,
            })),
            isLoading: false,
            hasError: false,
            errorMsg: "",
        };
    } catch (err) {
        return {
            pendingTransactions: [],
            txIdFilters: [],
            sourceAddressFilters: [],
            isLoading: false,
            hasError: true,
            errorMsg: (err as IFailureResponse).message,
        };
    }
}

export default async (req: NextApiRequest, res: NextApiResponse) => {
    res.status(200).json(await fetchPendingTransactions());
};
