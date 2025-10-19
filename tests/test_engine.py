# tests/test_engine.py
from unittest.mock import MagicMock
from backtester.engine import Backtester

def test_engine_uses_tminus1_signal(prices, broker, strategy, monkeypatch):
    # Force exactly one buy at t=10 by controlling signals
    fake_strategy = MagicMock()
    fake_strategy.signals.return_value = prices*0
    fake_strategy.signals.return_value.iloc[9] = 1  # triggers buy at t=10
    bt = Backtester(fake_strategy, broker)
    try:
        eq = bt.run(prices)
    except:
        AttributeError (f"Broker {broker} doesn't have any trade attribute")

    assert broker.position == 1
    assert broker.cash == 1000 - float(prices.iloc[10])