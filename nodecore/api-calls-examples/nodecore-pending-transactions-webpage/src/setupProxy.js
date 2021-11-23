const { createProxyMiddleware } = require('http-proxy-middleware');
const getUuid = require('uuid-by-string');

module.exports = (app) => {
    app.use(
        createProxyMiddleware('/get-pending-transactions', {
            target: process.env.REACT_APP_NODECORE_API_URL,
            pathRewrite: {
                '^/get-pending-transactions': '/api',
            },
            onProxyReq: (proxyReq, req) => {
                const call = proxyReq.getHeader('call');
                const requestId = proxyReq.getHeader('request-id');

                const callUuid = getUuid(`${call}${call.replace(/-/g, '')}`, 5);

                if (!requestId.includes(callUuid)) {
                    proxyReq.abort();
                }
            }
        }),
    );
};