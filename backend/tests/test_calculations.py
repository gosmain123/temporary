from app.services.calculations import surprise, moving_average, annualized_from_monthly, zscore, narrative_from_signals


def test_surprise() -> None:
    assert surprise(0.3, 0.2) == 0.1


def test_moving_average() -> None:
    assert moving_average([1.0, 2.0, 3.0]) == 2.0


def test_annualized() -> None:
    assert annualized_from_monthly([0.2, 0.2, 0.3]) > 2.0


def test_zscore_zero_sigma() -> None:
    assert zscore(1.0, [1.0, 1.0, 1.0]) == 0.0


def test_narrative() -> None:
    assert narrative_from_signals(0.3, 0.1, -0.1) == "Sticky inflation + resilient growth"
