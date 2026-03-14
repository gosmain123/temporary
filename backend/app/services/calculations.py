from statistics import mean, pstdev


def surprise(actual: float, consensus: float) -> float:
    return round(actual - consensus, 4)


def moving_average(values: list[float], window: int = 3) -> float:
    if len(values) < window:
        raise ValueError("Not enough data points")
    return round(mean(values[-window:]), 4)


def annualized_from_monthly(values: list[float], window: int = 3) -> float:
    if len(values) < window:
        raise ValueError("Not enough data points")
    avg = mean(values[-window:])
    return round(((1 + (avg / 100)) ** 12 - 1) * 100, 3)


def zscore(value: float, sample: list[float]) -> float:
    sigma = pstdev(sample)
    if sigma == 0:
        return 0.0
    return round((value - mean(sample)) / sigma, 4)


def narrative_from_signals(inflation: float, growth: float, liquidity: float) -> str:
    if inflation > 0.25 and growth > 0 and liquidity < 0:
        return "Sticky inflation + resilient growth"
    if inflation < 0.15 and growth < 0:
        return "Growth scare + fast disinflation"
    if inflation < 0.2 and growth > 0:
        return "Goldilocks"
    return "Stagflation"
