class SummaryRanges:

    def __init__(self):
        self.nums = [0] * 10002
        self.min = inf
        self.max = -inf

    def addNum(self, value: int) -> None:
        self.nums[value] = 1
        self.min = min(value, self.min)
        self.max = max(value, self.max)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        start = -1
        for i in range(self.min, self.max+2):
            if self.nums[i] > 0:
                if start < 0:
                    start = i
            else:
                if start > -1:
                    ans.append([start, i-1])
                    start = -1
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
