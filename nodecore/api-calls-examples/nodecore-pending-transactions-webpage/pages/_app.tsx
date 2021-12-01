import '../styles/globals.css';

import { Layout } from 'antd';
import Head from 'next/head';
import React from 'react';
import { GithubOutlined } from '@ant-design/icons';
import type { AppProps } from "next/app";
import { GITHUB_REPO } from 'utils/constants';

const { Header, Content, Footer } = Layout;

function MyApp({ Component, pageProps }: AppProps) {
  const company = "VeriBlock";
  const appTitle = `${company} MemPool`;
  // return <Component {...pageProps} />
  return (
    <>
      <Head>
        <title>{appTitle}</title>
        <meta name="description" content={appTitle} />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Layout className="layout">
        <Header>
          <div className="logo" />
          <div className="headerTitle">{appTitle}</div>
        </Header>
        <Content style={{ padding: "0 50px" }}>
          <div className="site-layout-content">
            <Component {...pageProps} />
          </div>
        </Content>
        <Footer style={{ textAlign: "center" }}>{company} © {(new Date()).getFullYear()} | <a href={GITHUB_REPO} target="_blank"
          rel="noreferrer" style={{ textDecoration: "none", color: "black" }}><GithubOutlined /> Github Repository</a></Footer>
      </Layout>
    </>
  );
}

export default MyApp;
