import pandas as pd

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run (self, prices: pd.Series):
        # Backtester: runs end-of-day loop: compute signal (t−1), trade at close (t), track cash/position/equity.
        # signals = self.strategy.generate_signals(prices)
        signals = self.strategy.signals.return_value
        history = []

        for i in range(1, len(prices)):
            date = prices.index[i]
            price = prices.iloc[i]
            signal = signals.iloc[i-1]  # yesterday’s signal → trade today
            if signal != 0:
                side = 'BUY' if signal == 1 else 'SELL'
                self.broker.market_order(side, 1, price)

            history.append({
                "date": date,
                "price": price,
                "cash": self.broker.cash,
                "position": self.broker.position,
            })
        return pd.DataFrame(history).set_index("date")
