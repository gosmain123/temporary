import type { TabPayload } from "@/lib/types";

export function ControlTower({ data }: { data: TabPayload }) {
  return (
    <section className="card">
      <h2 className="mb-3 text-lg font-semibold">Control Tower</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full text-sm">
          <thead>
            <tr className="text-left text-slate-400">
              <th>Series</th><th>Latest</th><th>Prev</th><th>Cons</th><th>Surprise</th><th>Trend</th><th>Regime</th><th>Impact</th>
            </tr>
          </thead>
          <tbody>
            {data.rows.map((row) => (
              <tr key={row.series} className="border-t border-slate-800">
                <td className="py-2">{row.series}</td>
                <td>{row.latest}</td>
                <td>{row.previous ?? "-"}</td>
                <td>{row.consensus ?? "-"}</td>
                <td>{row.surprise ?? "-"}</td>
                <td>{row.trend ?? "-"}</td>
                <td>{row.regime_signal ?? "-"}</td>
                <td>{row.market_impact ?? "-"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
