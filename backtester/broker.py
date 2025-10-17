class Broker:
    def __init__(self, cash: float = 1_000_000):
        self.cash = cash
        self.position = 0

    def market_order(self, side: str, qty: int, price: float):
        # Broker: accepts market orders, updates cash/position with no slippage/fees (keep deterministic for tests).
        
        delta = 1 # amt to add to our cash balance 

        if side == "BUY": 
            delta *= -1 
        
        delta = delta * qty * price 

        if cash + delta >= 0: 
            cash += delta 
            position = -delta
        else: 
            raise Exception (f"Could not complete order {side} of {qty} shares @ ${price}. Not enough balance.")
