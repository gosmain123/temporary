from datetime import datetime, timezone
import json
from pathlib import Path

from fastapi import APIRouter

from app.models import TabPayload, MetricRow, Narrative, OwnershipWarning, ConnectorStatus
from app.services.calculations import surprise, narrative_from_signals

router = APIRouter(prefix="/api", tags=["dashboard"])
SEED = json.loads(Path("data/seed.json").read_text())


@router.get("/control-tower", response_model=TabPayload)
def control_tower() -> TabPayload:
    now = datetime.now(timezone.utc)
    rows = []
    for item in SEED["control_tower"]:
        s = surprise(float(item["latest"]), float(item["consensus"]))
        rows.append(
            MetricRow(
                series=item["series"],
                latest=item["latest"],
                previous=item["previous"],
                consensus=item["consensus"],
                surprise=s,
                trend=item["trend"],
                regime_signal=item["regime_signal"],
                market_impact=item["market_impact"],
                last_updated=now,
            )
        )
    return TabPayload(tab="control_tower", rows=rows)


@router.get("/narrative", response_model=Narrative)
def narrative() -> Narrative:
    scenario = narrative_from_signals(inflation=0.3, growth=0.1, liquidity=-0.1)
    return Narrative(
        summary="Inflation surprises remain slightly hot while growth data is resilient and liquidity impulse is neutral-to-tight.",
        scenario=scenario,
        confidence=72,
    )


@router.get("/economic-calendar")
def economic_calendar() -> list[dict]:
    return SEED["calendar"]


@router.get("/ownership-warnings", response_model=list[OwnershipWarning])
def ownership_warnings() -> list[OwnershipWarning]:
    return [OwnershipWarning(**item) for item in SEED["ownership_warnings"]]


@router.get("/connectors", response_model=list[ConnectorStatus])
def connector_status() -> list[ConnectorStatus]:
    return [
        ConnectorStatus(name="FRED", status="live_if_key", notes="Live with FRED_API_KEY, mock fallback otherwise."),
        ConnectorStatus(name="BLS schedule", status="mock", notes="Adapter scaffolded; ingest job TODO."),
        ConnectorStatus(name="BEA schedule", status="mock", notes="Adapter scaffolded; ingest job TODO."),
        ConnectorStatus(name="Fed FOMC", status="mock", notes="Calendar seeded; connector TODO."),
        ConnectorStatus(name="Treasury auctions", status="mock", notes="Schedule/result connector TODO."),
        ConnectorStatus(name="CFTC COT", status="optional", notes="Delayed weekly; pluggable provider."),
        ConnectorStatus(name="SEC 13F", status="partial", notes="XML parser included; ingestion pipeline TODO."),
        ConnectorStatus(name="Market prices", status="optional", notes="Mock provider active, swappable adapter."),
    ]
