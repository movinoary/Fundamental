import Head from "next/head";
import React, { ReactNode } from "react";
import Footer from "../footer";
import Header from "../header";
import style from "./Layout.module.css";

interface LayoutProps {
  children: ReactNode;
  pageTitle: string;
}

export default function Layout(props: LayoutProps) {
  const { children, pageTitle } = props;

  return (
    <>
      <Head>
        <title>NextJs Basic || {pageTitle}</title>
        <meta name="description" content="Website NextJS Basic" />
      </Head>
      <div className={style.container}>
        <Header />
        <div className={style.content}>{children}</div>
        <Footer />
      </div>
    </>
  );
}
