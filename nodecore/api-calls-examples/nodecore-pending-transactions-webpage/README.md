This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

1. Create `.env.local` file with

```
NODECORE_API_URL=
```

You should put the full path to NodeCore API. For example: `NODECORE_API_URL=http://127.0.0.1:10600/api`

2. run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Docker

1. Create `.env.local` file with

```
NODECORE_API_URL=
NODECORE_API_PWD=
```

You should put the full path to NodeCore API. For example: `NODECORE_API_URL=http://127.0.0.1:10600/api`

If the **rpc.security.password.enabled** property in the _nodecore.properties_ file is set to to **true**, requests to the HTTP API will require the additional header **X-VBK-RPC-PASSWORD** to be set. The value of this header corresponds to the password defined in the property **rpc.security.password** in _nodecore.properties_. For example: `NODECORE_API_PWD=8Jvg@Y{m^WwdH&-N`

2. Build the container: `docker build . -t nodecore-pending-transactions-webpage`
   
3. Run it: `docker run -p 3000:3000 nodecore-pending-transactions-webpage`

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Next.js deployment documentation](https://nextjs.org/docs/deployment) - learn about deployment process

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!
