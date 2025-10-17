import pandas as pd
import numpy as np
from Strategy import Strategy

class VolatilityBreakoutStrategy(Strategy):

    def __init__ (self, window_size=20): 
        """
        Volatility Breakout Strategy 
        - Calculates a rolling x-day standard deviation of returns and buys when the current return is > this x-day figure. 
        
        Args:
            window: size of rolling window 
        """
        self.window_size = window_size
    
    def signals(self, prices: pd.Series) -> pd.Series:
        rolling_vols = prices.rolling(window=self.window_size).std()

        signals = [] # -1 to sell, 0 to hold/no action, 1 to buy 

        for i in range (len(rolling_vols)): 
            vol = rolling_vols[i] 
            price = prices[i] 

            if not vol: 
                signals.append(0) 
                continue 

            if price > vol: 
                signals.append(1) 
            elif price < vol: 
                signals.append(-1)
            else: 
                signals.append(0) 
        
        return signals 
