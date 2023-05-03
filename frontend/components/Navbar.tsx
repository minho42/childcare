import Link from "next/link";
import { useRouter } from "next/router";

export const Navbar = () => {
  const router = useRouter();

  return (
    <nav className="flex w-full items-center justify-center space-x-6 h-16 text-xl mb-3 font-medium">
      <Link href="/" passHref>
        <div
          className={`px-3 py-2 cursor-pointer
        ${router.pathname == "/" ? "" : ""}
        `}
        >
          Childcare Ratings
        </div>
      </Link>

      <Link href="/about" passHref>
        <div
          className={`px-3 py-2 cursor-pointer
        ${router.pathname == "/about" ? "" : ""}
        `}
        >
          About
        </div>
      </Link>
    </nav>
  );
};
