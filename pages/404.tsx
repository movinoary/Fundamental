import { useRouter } from "next/router";
import React, { useEffect } from "react";

export default function Custome404() {
  const Router = useRouter();

  useEffect(() => {
    setTimeout(() => {
      Router.push("/");
    }, 2000);
  }, []);

  return (
    <div>
      <h1 className="title-not-found">Oppsss....</h1>
      <h1 className="title-not-found">Halaman yang anda cari tidak ada</h1>
    </div>
  );
}
