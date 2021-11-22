import { IBitcoinBlockHeader } from './IBitcoinBlockHeader';
import { IOutput } from './IOutput';

export interface ITransaction {
    type: string;
    sourceAddress: string;
    sourceAmount: number;
    outputs: Array<IOutput>;
    transactionFee: number;
    data: string;
    bitcoinTransaction: string;
    endorsedBlockHeader: string;
    bitcoinBlockHeaderOfProof: IBitcoinBlockHeader;
    merklePath: string;
    contextBitcoinBlockHeaders: Array<IBitcoinBlockHeader>;
    timestamp: number;
    size: number;
    txId: string;
}

export interface ITransactionWithFeePerByte extends ITransaction {
    feePerByte: number;
}
