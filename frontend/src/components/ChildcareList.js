import { useState, useEffect } from "react";
import ChildcareItem from "./ChildcareItem";

const ChildcareList = () => {
  const [isSearching, setIsSearching] = useState(false);
  const [query, setQuery] = useState("");
  const [childcares, setChildcares] = useState([]);
  const [message, setMessage] = useState("");

  const pingHeroku = async () => {
    const res = await fetch("https://childcares.herokuapp.com");
    const { data } = await res.json();
    console.log(data);
  };

  useEffect(() => {
    pingHeroku();
  }, []);

  const handleFormSubmit = (e) => {
    e.preventDefault();
  };

  const handleSearchQueryChange = (e) => {
    setQuery(e.target.value.toLowerCase().trim());
  };

  const clearInput = () => {
    setQuery("");
    document.querySelector("#searchInput").focus();
  };

  const doSearch = async () => {
    if (query.length < 1) {
      setIsSearching(false);
      setChildcares([]);
      setMessage("");
      return;
    }

    setIsSearching(true);

    // const res = await fetch(`http://localhost:8000/search/?q=${query}`)
    const res = await fetch(`https://childcares.herokuapp.com/search/?q=${query}`);
    const searchedChildcares = await res.json();
    setChildcares(searchedChildcares);
    setIsSearching(false);

    if (searchedChildcares.length === 0) {
      setMessage("Not found");
    } else {
      setMessage("");
    }
  };

  return (
    <div className="flex flex-col justify-center pt-2 px-2">
      <div className="mx-3">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="search" className="text-center mb-1 mr-2">
            {isSearching ? <span> Searching... </span> : <span> Search </span>}
          </label>
          <div className="flex items-center justify-between relative">
            <input
              id="searchInput"
              value={query}
              onChange={handleSearchQueryChange}
              type="text"
              placeholder="Name or address"
              className="pl-6 pr-24 py-2 rounded-lg w-full border border-gray-300 focus:border-gray-500 bg-gray-100 focus:outline-none"
              autoFocus
            />

            <div>
              <button
                onClick={doSearch}
                className="absolute inset-y-0 right-0 h-full flex items-center  text-gray-500 hover:text-gray-800 px-3 py-2 rounded-lg focus:outline-none"
              >
                <svg
                  className="w-6 h-6"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  ></path>
                </svg>
              </button>

              {query && query.length > 0 ? (
                <div className="absolute inset-y-0 right-16 flex items-center">
                  <button
                    onClick={clearInput}
                    className="h-full px-3 text-gray-500 hover:text-gray-800 focus:outline-none"
                  >
                    <svg
                      className="w-6 h-6"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M6 18L18 6M6 6l12 12"
                      ></path>
                    </svg>
                  </button>
                </div>
              ) : (
                ""
              )}
            </div>
          </div>
        </form>
      </div>

      {childcares.map((childcare) => {
        return <ChildcareItem key={childcare.id} data={childcare} />;
      })}

      {message && message.length > 0 ? <div className="text-center py-3">{message}</div> : ""}
    </div>
  );
};

export default ChildcareList;
