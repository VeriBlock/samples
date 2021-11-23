import { API_PATH } from 'utils/constants';
import { IPendingTransactions } from 'models/IPendingTransactions';
import { request } from 'api/utils';

export const getPendingTransactions = async (): Promise<IPendingTransactions> => {
    return await request<IPendingTransactions>(
        API_PATH.PENDING_TRANSACTIONS.ENDPOINT,
        API_PATH.PENDING_TRANSACTIONS.METHOD
    );
};
