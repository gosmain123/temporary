export function NarrativePanel({ summary, scenario, confidence }: { summary: string; scenario: string; confidence: number }) {
  return (
    <section className="card">
      <p className="label">Current market narrative</p>
      <h3 className="mt-1 text-base font-semibold">{scenario} (confidence {confidence}%)</h3>
      <p className="mt-2 text-sm text-slate-300">{summary}</p>
    </section>
  );
}
