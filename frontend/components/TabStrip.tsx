export function TabStrip({ items }: { items: string[] }) {
  return (
    <div className="card overflow-x-auto">
      <div className="flex min-w-max gap-2">
        {items.map((item) => (
          <span key={item} className="rounded-full border border-slate-700 px-3 py-1 text-xs text-slate-300">
            {item}
          </span>
        ))}
      </div>
    </div>
  );
}
