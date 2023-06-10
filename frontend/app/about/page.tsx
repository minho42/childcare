import { formatDistance } from "date-fns";

type Stats = {
  lastUpdate: string;
  totalCount: number;
};

async function getStats() {
  const res = await fetch("http://127.0.0.1:8000/stats");
  const data: Stats = await res.json();
  return data;
}

export default async function About() {
  const stats = await getStats();
  let lastUpdate;
  if (stats.lastUpdate) {
    if (new Date().valueOf() - new Date(stats.lastUpdate).valueOf() >= 30 * 1000 * 1) {
      lastUpdate = formatDistance(new Date(stats.lastUpdate), new Date(), {
        includeSeconds: false,
        addSuffix: true,
      });
    } else {
      lastUpdate = "Currently being synced...";
    }
  }

  return (
    <div className="flex flex-col items-center justify-center px-6 mt-3">
      <div className="text-xl font-semibold leading-8 mb-3">National Quality Standard ratings</div>

      <div className="flex flex-col mb-3">
        <div className="flex flex-wrap">
          Data from:
          <a
            href="https://www.acecqa.gov.au/resources/national-registers/services"
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
        {stats.totalCount ? <div>Total: {stats.totalCount}</div> : <div>loading...</div>}
      </div>
    </div>
  );
}
