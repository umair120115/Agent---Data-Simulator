#All mathematival tools 
class MathTool:
    def market_value(self, shares, price):
        return round(shares * price, 2)

    def profit_loss(self, shares, buy, current):
        return round((current - buy) * shares, 2)

