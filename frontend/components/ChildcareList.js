import { useRef, useState, useEffect } from "react";
import { ChildcareItem } from "./ChildcareItem";
import { SearchIcon } from "@heroicons/react/outline";

export const ChildcareList = () => {
  const [isSearching, setIsSearching] = useState(false);
  const [childcares, setChildcares] = useState([]);
  const [message, setMessage] = useState("");
  const inputRef = useRef();

  useEffect(() => {}, []);

  const handleFormSubmit = (e) => {
    e.preventDefault();
  };

  const doSearch = async () => {
    const query = inputRef.current.value.trim();
    if (query.length < 1) {
      setIsSearching(false);
      setChildcares([]);
      setMessage("");
      return;
    }

    setIsSearching(true);

    const res = await fetch(`http://localhost:8000/search/?q=${query}`);
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
              ref={inputRef}
              id="searchInput"
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
