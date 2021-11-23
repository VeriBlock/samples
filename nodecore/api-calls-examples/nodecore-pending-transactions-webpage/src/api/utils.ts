/* eslint-disable  @typescript-eslint/no-non-null-assertion */
/* eslint-disable  @typescript-eslint/no-explicit-any */

import { IJsonRPC } from 'models/IJsonRPC';

export const request = async <T>(method: string, params = {}): Promise<T> => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');

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

    const response = await window.fetch('/api', requestOptions);

    if (response.status === 200) {
        return ((await response.json()) as any as IJsonRPC<T>).result;
    }

    if (response.status === 401) {
        return Promise.reject({
            status: 401,
            message: 'Auth needed'
        });
    }

    return Promise.reject({
        status: response.status,
        message: (JSON.parse((await response.text()) as unknown as string) as any).message
    });
};
