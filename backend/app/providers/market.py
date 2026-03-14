class MockMarketProvider:
    async def latest_snapshot(self) -> dict:
        return {
            "UST2Y": 4.29,
            "UST10Y": 3.91,
            "DXY": 103.6,
            "WTI": 78.2,
            "VIX": 15.8,
            "HY_OAS": 352,
        }
