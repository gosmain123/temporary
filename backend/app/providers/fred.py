import os
import httpx


class FredProvider:
    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self) -> None:
        self.api_key = os.getenv("FRED_API_KEY", "")

    async def fetch_series(self, series_id: str) -> dict:
        if not self.api_key:
            return {"series_id": series_id, "status": "mock", "observations": []}
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
            "sort_order": "desc",
            "limit": 12,
        }
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
