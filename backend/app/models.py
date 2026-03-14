from datetime import datetime
from pydantic import BaseModel


class MetricRow(BaseModel):
    series: str
    latest: float | str
    previous: float | str | None = None
    consensus: float | str | None = None
    surprise: float | str | None = None
    three_month_avg: float | str | None = None
    three_month_annualized: float | str | None = None
    trend: str | None = None
    regime_signal: str | None = None
    market_impact: str | None = None
    last_updated: datetime
    delayed: bool = False


class TabPayload(BaseModel):
    tab: str
    rows: list[MetricRow]


class Narrative(BaseModel):
    summary: str
    scenario: str
    confidence: int


class OwnershipWarning(BaseModel):
    label: str
    detail: str


class ConnectorStatus(BaseModel):
    name: str
    status: str
    notes: str
