import { useState, useEffect } from "react";
import { formatDistance } from "date-fns";

const About = () => {
  const [lastUpdate, setLastUpdate] = useState("loading...");
  const [totalCount, setTotalCount] = useState("loading...");
  const getStats = async () => {
    const res = await fetch("https://childcares.herokuapp.com/stats");
    const stats = await res.json();

    if (stats.lastUpdate) {
      if (new Date() - new Date(stats.lastUpdate) >= 30 * 1000 * 1) {
        setLastUpdate(formatDistance(new Date(stats.lastUpdate), new Date()) + " ago");
      } else {
        setLastUpdate("currently being synced...");
      }
    }
    if (stats.totalCount) {
      setTotalCount(stats.totalCount);
    }
  };

  useEffect(() => {
    getStats();
  }, []);

  return (
    <div className="flex flex-col items-center justify-center px-6 mt-3">
      <div className="text-xl font-semibold leading-8 mb-3">National Quality Standard ratings</div>

      <div className="flex flex-col mb-3">
        <div className="flex flex-wrap">
          Data from:
          <a
            href="https://www.acecqa.gov.au/resources/national-registers/services?s=&f%5B0%5D=service_state%3ANSW"
            target="_blank"
            rel="noopener noreferrer"
            className="items-center text-blue-700 underline ml-2"
          >
            acecqa.gov.au
          </a>
        </div>

        <div className="flex flex-wrap">
          See also:
          <a
            href="https://www.childcarefinder.gov.au"
            target="_blank"
            rel="noopener noreferrer"
            className="items-center text-blue-700 underline ml-2"
          >
            childcarefinder.gov.au
          </a>
        </div>

        <div className="mt-2 mb-3">
          <p className="font-bold">Quality areas</p>
          <p>1. Educational program and practice</p>
          <p>2. Children's health and safety</p>
          <p>3. Physical environment</p>
          <p>4. Staffing arrangements</p>
          <p>5. Relationships with children</p>
          <p>6. Collaborative partnerships with families and communities</p>
          <p>7. Governance and leadership</p>
        </div>
      </div>

      <div className="mb-3">
        {lastUpdate ? <div>Synced: {lastUpdate}</div> : ""}
        {totalCount ? <div>Total: {totalCount}</div> : <div>loading...</div>}
      </div>

      <div className="flex space-x-4 mb-6">
        <div>
          <a
            href="https://twitter.com/minhokim42"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center text-blue-700 underline ml-1"
          >
            twitter
          </a>
        </div>
      </div>
    </div>
  );
};

export default About;
