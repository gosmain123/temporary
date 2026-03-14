# U.S. Macro + Market Intelligence Dashboard

Production-oriented starter project for an investor/PM workflow with:
- **Frontend**: Next.js 15 + TypeScript + Tailwind + Recharts-ready UI skeleton
- **Backend**: FastAPI + Pydantic + provider abstractions
- **Cache/storage target**: SQLite for local dev (pluggable to Postgres later)
- **Data architecture**: official-source-first adapters + mock fallbacks

## What is implemented now

- Multi-tab institutional dashboard shell (Control Tower through Playbook tabs).
- Control Tower table with KPI fields: latest/prev/consensus/surprise/trend/regime/impact.
- Rule-based market narrative API (no LLM dependency).
- Provider interfaces and adapters:
  - FRED adapter (`live_if_key` with fallback)
  - mock market snapshot adapter
  - SEC 13F XML information table parser
- Delayed-data warnings for **13F** and **COT** built into UI and API.
- Seeded backend data so app works before all connectors are wired.
- Tests for core calculations + 13F parser.

## Repo structure

```text
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── parsers/sec_13f.py
│   │   ├── providers/{base.py, fred.py, market.py}
│   │   ├── routers/dashboard.py
│   │   └── services/calculations.py
│   ├── data/seed.json
│   ├── tests/{test_calculations.py, test_sec_parser.py}
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app/{layout.tsx, page.tsx, globals.css}
│   ├── components/{TabStrip.tsx, ControlTower.tsx, NarrativePanel.tsx}
│   ├── lib/{types.ts, mock-data.ts}
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
├── .env.example
├── Makefile
└── docker-compose.yml
```

## Run locally (without Docker)

### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
corepack enable
pnpm install
pnpm dev
```

Open: `http://localhost:3000`

## Run with Makefile

```bash
make backend
make frontend
make test
```

## Run with Docker

```bash
docker compose up --build
```

## Connector status

### Fully live
- FastAPI API surface + local seed-backed endpoints.
- Rule-based narrative engine.
- 13F XML information-table parser.

### Live if configured
- FRED connector (requires `FRED_API_KEY`).

### Mocked
- BLS/BEA/Fed/Treasury schedule ingestion jobs (scaffolded via architecture, seeded examples).
- Market prices default adapter.

### Optional / pluggable
- ETF flows, options/gamma/skew, short interest, earnings revisions, PB-style positioning proxies.

## Data caveats

- **13F**: delayed ownership disclosure (up to 45 days after quarter-end), partial picture of exposures.
- **COT**: delayed weekly positioning (Tuesday reference, Friday release).

## Testing

```bash
cd backend
pytest -q
```

## Next 10 highest-impact improvements

1. Implement persistent SQLite schema and ETL jobs with TTL metadata per dataset.
2. Add APScheduler/Celery periodic refresh workers and retry/backoff logic.
3. Add full economic calendar ingestion (BLS/BEA/Fed/Treasury) with timezone conversion ET/SGT.
4. Build complete tab-specific APIs and CSV export endpoints.
5. Implement full 13F filing ingestion pipeline from EDGAR index + manager history.
6. Add CFTC COT parser and crowdedness z-score pipeline.
7. Add scenario engine with trigger rules + confidence scoring across all tabs.
8. Add authentication and saved watchlists/notes.
9. Add frontend charting panels with Recharts across all tabs.
10. Add integration tests and containerized CI workflow.
