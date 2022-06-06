import Layout from "../../components/layout";
import { useRouter } from "next/router";
import style from "../../styles/Users.module.css";

interface UserProps {
  dataUsers: Array<any>;
}

export default function Users(props: UserProps) {
  const { dataUsers } = props;
  const router = useRouter();

  console.log(dataUsers);

  return (
    <Layout pageTitle="User">
      {dataUsers.map(user => {
        return (
          <div
            key={user.id}
            onClick={() => router.push(`/user/${user.id}`)}
            className={style.card}
          >
            <p>Nama : {user.name}</p>
            <p>Email : {user.email}</p>
          </div>
        );
      })}
    </Layout>
  );
}

export async function getStaticProps() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  const dataUsers = await res.json();

  return {
    props: {
      dataUsers,
    },
  };
}
