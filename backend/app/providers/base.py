from typing import Protocol


class TimeSeriesProvider(Protocol):
    async def fetch_series(self, series_id: str) -> dict: ...


class OptionalMarketProvider(Protocol):
    async def latest_snapshot(self) -> dict: ...
