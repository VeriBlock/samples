import "../styles/globals.css";
import type { AppProps } from "next/app";
import React from "react";
import { Layout } from "antd";
import Head from "next/head";

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
        <Footer style={{ textAlign: "center" }}>{company} © 2021</Footer>
      </Layout>
    </>
  );
}

export default MyApp;
