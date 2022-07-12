import { v4 as uuidv4 } from "uuid";
import { useState, useEffect } from "react";
import { Chart } from "./Chart";
import { ArrowRightIcon } from "@heroicons/react/outline";

export const ChildcareItem = ({
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
      className="flex flex-col py-3 px-1 sm:mx-4 bg-white border-b border-gray-300 space-y-4"
      style={{ touchAction: "manipulation" }}
    >
      <div className="flex flex-col gap-2">
        <div className="text-2xl font-medium">{name}</div>
        <div className="text-gray-500">
          {address} {suburb} {state} {postcode}
        </div>
      </div>

      <div className="flex flex-col items-center justify-center">
        <div className="flex ">
          <div className="text-xl font-medium">{overall_rating}</div>
        </div>

        <div className="flex flex-row mt-1">
          {prev_average_ratings && prev_average_ratings > 0 ? (
            <div className="flex items-center ml-2">
              <div className="flex flex-col items-center">
                <div className="text-2xl border-2 border-transparent bg-gray-100 rounded-lg px-3 py-2">
                  {prev_average_ratings}
                </div>
                <div className="">{prev_ratings_issued}</div>
              </div>

              <div className="ml-1 mb-5">
                <ArrowRightIcon className="w-6 h-6" />
              </div>
            </div>
          ) : (
            ""
          )}

          {average_ratings && average_ratings > 0 ? (
            <div className="flex flex-col items-center justify-center ml-1">
              <div className="text-2xl border-2 border-black rounded-lg px-3 py-2">{average_ratings}</div>
              <div className="">{ratings_issued}</div>
            </div>
          ) : (
            ""
          )}
        </div>
      </div>

      <div className="flex">
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
