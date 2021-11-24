export interface IJsonRPC<T> {
    id: number;
    jsonrpc: string;
    result: T;
}
