/* eslint-disable  @typescript-eslint/no-non-null-assertion */
/* eslint-disable  @typescript-eslint/no-explicit-any */

import { IJsonRPC } from 'models/IJsonRPC';
import { isJsonValid } from 'utils/utils';

export const request = async <T>(method: string, params = {}): Promise<T> => {
    
    if (!process.env.NODECORE_API_URL) {
        return Promise.reject({
            status: 501,
            message: 'You need to specify the NodeCore API Url'
        });
    }

    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    
    if (process.env.NODECORE_API_PWD) {
        myHeaders.append('X-VBK-RPC-PASSWORD', process.env.NODECORE_API_PWD);
    }

    const raw = JSON.stringify({
        jsonrpc: '2.0',
        method: method,
        params: params,
        id: 1
    });

    const requestOptions: RequestInit = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    const response = await fetch(process.env.NODECORE_API_URL, requestOptions);

    if (response.status === 200) {
        return ((await response.json()) as any as IJsonRPC<T>).result;
    }

    if (response.status === 401) {
        return Promise.reject({
            status: 401,
            message: 'Auth needed'
        });
    }

    const responseText = await response.text();

    return Promise.reject({
        status: response.status,
        message: isJsonValid(responseText) ? (JSON.parse((responseText) as unknown as string) as any).message : responseText
    });
};