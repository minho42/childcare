import { v4 as uuidv4 } from "uuid";

export const ChartItem = ({ area, rating }) => {
  const ratingTexts = [
    "Significant Improvement required",
    "Working Towards NQS",
    "Meeting NQS",
    "Exceeding NQS",
    "Excellent",
  ];
  const tempArray = new Array(rating).fill(0);
  return (
    <div>
      <div className="flex flex-col items-center">
        <div className="">{rating}</div>
        {tempArray.map((item) => {
          return (
            <div
              key={uuidv4()}
              className={`w-6 h-6 rounded-sm ${
                rating >= 4
                  ? "bg-green-400"
                  : rating >= 3
                  ? "bg-amber-300"
                  : rating >= 2
                  ? "bg-red-300"
                  : "bg-gray-200"
              }  mt-px mb-px`}
            ></div>
          );
        })}
        <div className="">{area.slice(0, 1)}</div>
      </div>
    </div>
  );
};
