import { useState, useEffect } from "react";
import { ChildcareItem } from "./ChildcareItem";
import { SearchIcon, XIcon } from "@heroicons/react/outline";

export const ChildcareList = () => {
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
    setQuery(e.target.value.toLowerCase());
  };

  const clearInput = () => {
    setQuery("");
    document.querySelector("#searchInput").focus();
  };

  const doSearch = async () => {
    const trimmedQuery = query.trim();
    if (trimmedQuery.length < 1) {
      setIsSearching(false);
      setChildcares([]);
      setMessage("");
      return;
    }

    setIsSearching(true);

    // const res = await fetch(`http://localhost:8000/search/?q=${trimmedQuery}`)
    const res = await fetch(`https://childcares.herokuapp.com/search/?q=${trimmedQuery}`);
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
    <div className="flex flex-col justify-center pt-2 px-2 space-y-3">
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
                className="absolute inset-y-0 right-0 h-full flex items-center text-gray-500 hover:text-black px-3 py-2 rounded-lg focus:outline-none"
              >
                <SearchIcon className="w-7 h-7" />
              </button>

              {query && query.length > 0 ? (
                <div className="absolute inset-y-0 right-12 flex items-center">
                  <button
                    onClick={clearInput}
                    className="h-full px-3 text-gray-500 hover:text-gray-800 focus:outline-none"
                  >
                    <XIcon className="w-7 h-7" />
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
