import { API_PATH } from 'utils/constants';
import { IPendingTransactions } from 'models/IPendingTransactions';
import { request } from 'api/utils';
import { IFailureResponse } from 'models/IFailureResponse';

export const getPendingTransactions = async (): Promise<IPendingTransactions | IFailureResponse> => (
    await request<IPendingTransactions | IFailureResponse>(
        API_PATH.PENDING_TRANSACTIONS
    )
);
