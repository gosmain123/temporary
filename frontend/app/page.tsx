import { ControlTower } from "@/components/ControlTower";
import { NarrativePanel } from "@/components/NarrativePanel";
import { TabStrip } from "@/components/TabStrip";
import { fallbackControlTower, tabs } from "@/lib/mock-data";
import type { TabPayload } from "@/lib/types";

const API = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

async function getControlTower(): Promise<TabPayload> {
  try {
    const res = await fetch(`${API}/api/control-tower`, { cache: "no-store" });
    if (!res.ok) return fallbackControlTower;
    return (await res.json()) as TabPayload;
  } catch {
    return fallbackControlTower;
  }
}

async function getNarrative(): Promise<{ summary: string; scenario: string; confidence: number }> {
  try {
    const res = await fetch(`${API}/api/narrative`, { cache: "no-store" });
    if (!res.ok) throw new Error("fallback");
    return (await res.json()) as { summary: string; scenario: string; confidence: number };
  } catch {
    return {
      summary: "Fallback narrative from local seed data.",
      scenario: "Goldilocks",
      confidence: 55,
    };
  }
}

async function getConnectorStatus(): Promise<Array<{ name: string; status: string; notes: string }>> {
  try {
    const res = await fetch(`${API}/api/connectors`, { cache: "no-store" });
    if (!res.ok) return [];
    return (await res.json()) as Array<{ name: string; status: string; notes: string }>;
  } catch {
    return [];
  }
}

export default async function Home() {
  const [control, narrative, connectors] = await Promise.all([
    getControlTower(),
    getNarrative(),
    getConnectorStatus(),
  ]);

  return (
    <main className="mx-auto grid w-[min(1200px,95vw)] gap-4 py-6">
      <header className="card">
        <p className="label">Production-grade macro + market intelligence</p>
        <h1 className="mt-1 text-2xl font-bold">U.S. Macro Dashboard</h1>
        <p className="mt-2 text-sm text-slate-300">Institutional layout: regime, policy gap, market pricing, positioning, delayed ownership caveats.</p>
      </header>

      <TabStrip items={tabs} />
      <NarrativePanel summary={narrative.summary} scenario={narrative.scenario} confidence={narrative.confidence} />
      <ControlTower data={control} />

      <section className="card">
        <h2 className="mb-2 text-lg font-semibold">Connector status (live vs mocked vs optional)</h2>
        <ul className="grid gap-2 text-sm">
          {connectors.map((c) => (
            <li key={c.name} className="rounded border border-slate-800 p-2">
              <strong>{c.name}</strong>: <span className="uppercase">{c.status}</span> — {c.notes}
            </li>
          ))}
        </ul>
      </section>

      <section className="card">
        <h2 className="mb-2 text-lg font-semibold">Delayed dataset warning</h2>
        <ul className="list-disc pl-5 text-sm text-slate-300">
          <li>13F ownership is delayed up to 45 days from quarter-end and does not capture real-time conviction.</li>
          <li>CFTC COT is delayed weekly positioning (Tuesday snapshot, Friday publication).</li>
        </ul>
      </section>
    </main>
  );
}
