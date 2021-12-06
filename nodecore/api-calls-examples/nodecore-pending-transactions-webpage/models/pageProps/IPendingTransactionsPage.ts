import { ITableFilter } from "models/ITableFilter";
import { ITransactionWithFeePerByteAndGmtDate } from "models/ITransaction";

export interface IPendingTransactionsPage {
    pendingTransactions: Array<ITransactionWithFeePerByteAndGmtDate>;
    txIdFilters: Array<ITableFilter>;
    sourceAddressFilters: Array<ITableFilter>;
    isLoading: boolean;
    hasError: boolean;
    errorMsg: string;
}