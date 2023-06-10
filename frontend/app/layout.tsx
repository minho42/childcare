import "./globals.css";
import Link from "next/link";

export const metadata = {
  title: "Childcare Ratings",
  description: "ACECQA Ratings",
};

function Navbar() {
  return (
    <nav className="flex w-full items-center justify-center space-x-6 h-16 text-2xl mb-3">
      <Link href="/">
        <div className="px-3 py-2 cursor-pointer">Childcare Ratings</div>
      </Link>

      <Link href="/about">
        <div className="px-3 py-2 cursor-pointer">About</div>
      </Link>
    </nav>
  );
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
