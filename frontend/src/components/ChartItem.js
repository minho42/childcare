import { v4 as uuidv4 } from "uuid";
import ReactTooltip from "react-tooltip";

const ChartItem = ({ area, rating }) => {
  const ratingTexts = [
    "Significant Improvement required",
    "Working Towards NQS",
    "Meeting NQS",
    "Exceeding NQS",
    "Excellent",
  ];
  const tempArray = new Array(rating).fill(0);
  const uniqueId = uuidv4();
  return (
    <div>
      <div data-tip data-for={uniqueId} className="flex flex-col items-center">
        <div className="text-sm text-gray-400">{rating}</div>
        {tempArray.map((item) => {
          return <div key={uuidv4()} className="w-4 h-3 bg-yellow-200 border-t-2 border-white"></div>;
        })}
        <div className="text-xs text-gray-400">{area.slice(0, 1)}</div>
      </div>
      <ReactTooltip id={uniqueId} place="top" effect="solid">
        {area}: {ratingTexts[rating - 1]}
      </ReactTooltip>
    </div>
  );
};

export default ChartItem;
