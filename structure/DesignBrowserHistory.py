class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = 0
        self.max = 0
        self.history = [None] * 5000
        self.history[self.curr] = homepage

    def visit(self, url: str) -> None:
        self.curr += 1
        self.max = self.curr
        self.history[self.curr] = url

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.max)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
