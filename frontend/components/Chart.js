import { v4 as uuidv4 } from "uuid";
import { ChartItem } from "./ChartItem";

export const Chart = ({ ratings }) => {
  const qualityAreas = [
    "1. Educational program and practice",
    "2. Children's health and safety",
    "3. Physical environment",
    "4. Staffing arrangements",
    "5. Relationships with children",
    "6. Collaborative partnerships with families and communities",
    "7. Governance and leadership",
  ];

  return (
    <div className="flex items-end justify-center space-x-3">
      {ratings.map((rating, i) => {
        return <ChartItem key={uuidv4()} area={qualityAreas[i]} rating={rating} className="" />;
      })}
    </div>
  );
};
