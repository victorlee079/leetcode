class StockSpanner:

    def __init__(self):
        self.stk = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stk and self.stk[-1][0] <= price:
            p, s = self.stk.pop()
            span += s
        self.stk.append((price, span))
        return cnt
