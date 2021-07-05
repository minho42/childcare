import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <header className="bg-white border-b border-gray-300 shadow-sm">
        <div className="flex items-center justify-between pl-3 py-2 h-12">
          <div className="flex items-center">
            <Link to="/" className="px-1 py-1 font-semibold">
              Childcare Ratings - NSW
            </Link>
          </div>
          <div className="mr-3">
            <Link
              to="/about"
              className="block px-3 py-2 ml-2 text-center rounded-lg border-none hover:bg-gray-200"
            >
              About
            </Link>
          </div>
        </div>
      </header>
    </nav>
  );
};

export default Navbar;
