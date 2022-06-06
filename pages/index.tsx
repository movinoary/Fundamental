import type { NextPage } from "next";
import Image from "next/image";
import Layout from "../components/layout";
import style from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <Layout pageTitle="Home Page">
      <Image src="/profile.jpg" alt="profile" width={200} height={200} />
      <h1 className={style["title-homepage"]}>Welcome Vino</h1>;
    </Layout>
  );
};

export default Home;
