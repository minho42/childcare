import { v4 as uuidv4 } from "uuid";
import { useState, useEffect } from "react";
import Chart from "./Chart";

const ChildcareItem = ({
  data: {
    id,
    name,
    address,
    suburb,
    state,
    postcode,
    overall_rating,
    ratings_issued,
    prev_ratings_issued,
    average_ratings,
    prev_average_ratings,
    rating1,
    rating2,
    rating3,
    rating4,
    rating5,
    rating6,
    rating7,
  },
}) => {
  const [ratings, setRatings] = useState([]);

  useEffect(() => {
    setRatings([rating1, rating2, rating3, rating4, rating5, rating6, rating7]);
  }, [rating1, rating2, rating3, rating4, rating5, rating6, rating7]);

  return (
    <div
      className="flex flex-col pt-3 pb-4 px-1 sm:mx-4 bg-white border-b border-gray-300 "
      style={{ touchAction: "manipulation" }}
    >
      <div className="flex justify-between">
        <div>
          <div className="font-medium">{name}</div>
          <div className="mt-1 text-base text-gray-500 hidden sm:flex">{address}</div>
          <div className="mt-1 text-base text-gray-500">
            {suburb} {state} {postcode}
          </div>
        </div>
        <div className="flex flex-col">
          <div className="flex justify-end text-right">
            <div className="">{overall_rating}</div>
          </div>

          <div className="flex flex-row justify-end mt-1">
            {prev_average_ratings && prev_average_ratings > 0 ? (
              <div className="flex items-center ml-2">
                <div className="flex flex-col items-center">
                  <div className="tracking-wider bg-gray-100 rounded-lg px-3 py-2">
                    {prev_average_ratings}
                  </div>
                  <div className="text-sm text-gray-500">{prev_ratings_issued}</div>
                </div>

                <div className="ml-1">
                  <svg
                    className="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M14 5l7 7m0 0l-7 7m7-7H3"
                    ></path>
                  </svg>
                </div>
              </div>
            ) : (
              ""
            )}

            {average_ratings && average_ratings > 0 ? (
              <div className="flex flex-col items-center justify-center ml-1">
                <div className="tracking-wider bg-yellow-200 rounded-lg px-3 py-2">{average_ratings}</div>
                <div className="text-sm text-gray-500">{ratings_issued}</div>
              </div>
            ) : (
              ""
            )}
          </div>
        </div>
      </div>
      <div className="flex justify-end mt-2">
        {average_ratings > 0 ? (
          <div className="w-full">
            <Chart key={uuidv4()} ratings={ratings} />
          </div>
        ) : (
          ""
        )}
      </div>
    </div>
  );
};

export default ChildcareItem;
