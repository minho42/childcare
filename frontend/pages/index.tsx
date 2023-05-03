import Head from "next/head";
import { ChildcareList } from "../components/ChildcareList";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Childcare Ratings</title>
        <meta name="description" content="Childcare Ratings" />
      </Head>
      <ChildcareList />
    </div>
  );
}
