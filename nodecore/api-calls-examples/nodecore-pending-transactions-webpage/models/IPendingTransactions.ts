import { IReply } from './IReply';
import { ITransaction } from './ITransaction';

export interface IPendingTransactions extends IReply {
    transactions: Array<ITransaction>;
}
