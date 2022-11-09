class StockSpanner:

    def __init__(self):
        self.stk = []
        

    def next(self, price: int) -> int:
        cnt = 1
        while self.stk and self.stk[-1][0] <= price:
            p, c = self.stk.pop()
            cnt += c
        self.stk.append((price, cnt))
        return cnt
