import { API_PATH } from '../constants';
import { IPendingTransactions } from '../models/IPendingTransactions';
import { request } from './utils';

export const getPendingTransactions = async (): Promise<IPendingTransactions> => {
    return await request<IPendingTransactions>(API_PATH.PENDING_TRANSACTIONS);
};
