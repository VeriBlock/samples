import { IResult } from './IResult';

export interface IReply {
    success: boolean;
    results: Array<IResult>;
}
