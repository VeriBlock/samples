import { Modal, Table } from "antd";
import { SortOrder } from "antd/lib/table/interface";
import { getPendingTransactions } from "api/pendingTransactions";
import { IFailureResponse } from "models/IFailureResponse";
import { IPendingTransactions } from "models/IPendingTransactions";
import { ITableFilter } from "models/ITableFilter";
import { ITransactionWithFeePerByte } from "models/ITransaction";
import type { GetStaticProps, NextPage } from "next";
import React from "react";
import { EXPLORER_TX_SEARCH_URL } from "utils/constants";

interface PendingTransactionsPageProps {
  pendingTransactions: Array<ITransactionWithFeePerByte>;
  txIdFilters: Array<ITableFilter>;
  sourceAddressFilters: Array<ITableFilter>;
  isLoading: boolean;
  hasError: boolean;
  errorMsg: string;
}

const PendingTransactionsPage: NextPage<PendingTransactionsPageProps> = ({
  pendingTransactions,
  txIdFilters,
  sourceAddressFilters,
  isLoading,
  hasError,
  errorMsg,
}) => {
  const columns = [
    {
      title: "Transaction ID",
      dataIndex: "txId",
      key: "txId",
      filters: txIdFilters,
      onFilter: (
        value: string | number | boolean,
        record: ITransactionWithFeePerByte
      ) => record.txId.startsWith(value as string),
      filterSearch: true,
      render: (txId: string) => (
        <a
          href={`${EXPLORER_TX_SEARCH_URL}${txId}`}
          target="_blank"
          rel="noreferrer"
        >
          {`${txId.slice(0, 5)}...${txId.slice(txId.length - 5)}`}
        </a>
      ),
    },
    {
      title: "Source Address",
      dataIndex: "sourceAddress",
      key: "sourceAddress",
      filters: sourceAddressFilters,
      onFilter: (
        value: string | number | boolean,
        record: ITransactionWithFeePerByte
      ) => record.sourceAddress.startsWith(value as string),
      filterSearch: true,
    },
    {
      title: "Fee per byte",
      dataIndex: "feePerByte",
      key: "feePerByte",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      defaultSortOrder: "descend" as SortOrder,
      sorter: (a: ITransactionWithFeePerByte, b: ITransactionWithFeePerByte) =>
        a.feePerByte - b.feePerByte,
      render: (feePerByte: number) => feePerByte.toFixed(8),
    },
    {
      title: "Fee",
      dataIndex: "transactionFee",
      key: "transactionFee",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      sorter: (a: ITransactionWithFeePerByte, b: ITransactionWithFeePerByte) =>
        a.transactionFee - b.transactionFee,
    },
    {
      title: "Size",
      dataIndex: "size",
      key: "size",
      sortDirections: ["descend", "ascend"] as Array<SortOrder>,
      sorter: (a: ITransactionWithFeePerByte, b: ITransactionWithFeePerByte) =>
        a.size - b.size,
    },
  ];

  if (hasError) {
    Modal.error({
      title: "Error",
      content: errorMsg,
    });
  }

  return (
    <Table
      loading={isLoading}
      columns={columns}
      dataSource={pendingTransactions}
      rowKey="txId"
    />
  );
};

export const getStaticProps: GetStaticProps = async () => {
  const pendingTransactionsResponse: IPendingTransactions | IFailureResponse =
    await getPendingTransactions();

  if (Object.keys(pendingTransactionsResponse).indexOf("message") > -1) {
    return {
      props: {
        pendingTransactions: [],
        txIdFilters: [],
        sourceAddressFilters: [],
        isLoading: false,
        hasError: true,
        errorMsg: (pendingTransactionsResponse as IFailureResponse).message,
      },
    };
  }

  return {
    props: {
      pendingTransactions: (
        pendingTransactionsResponse as IPendingTransactions
      ).transactions.map(
        (transaction) =>
          ({
            ...transaction,
            feePerByte: transaction.transactionFee / transaction.size,
          } as ITransactionWithFeePerByte)
      ),
      txIdFilters: (
        pendingTransactionsResponse as IPendingTransactions
      ).transactions.map((transaction) => ({
        text: transaction.txId,
        value: transaction.txId,
      })),
      sourceAddressFilters: (
        pendingTransactionsResponse as IPendingTransactions
      ).transactions.map((transaction) => ({
        text: transaction.sourceAddress,
        value: transaction.sourceAddress,
      })),
      isLoading: false,
      hasError: false,
      errorMsg: "",
    },
  };
};

export default PendingTransactionsPage;
