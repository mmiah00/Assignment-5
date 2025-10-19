import random
import pandas as pd

class Loader:
    def __init__(self):
        self.prices = pd.Series()

    def load_data(self, n):
        x = 10
        drift = 2
        prices = []
        for i in range(n):
            x = random.randint(-3, 3) + drift + x
            if x > 1:
                prices.append(x)
        self.prices = pd.Series(prices)
        return self.prices

prices = Loader()
print(prices.load_data(25))