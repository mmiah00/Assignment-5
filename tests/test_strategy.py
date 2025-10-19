def test_signals_length(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)

def test_signals_bounds(strategy, prices):
    sig = strategy.signals(prices)
    assert min(sig) == 0 #owed to monotonically rising prices
    assert max(sig) == 1
