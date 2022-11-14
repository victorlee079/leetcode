from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        n = len(self.sl)
        half = n // 2
        if n % 2 == 0:
            return (self.sl[half - 1] + self.sl[half]) / 2
        else:
            return self.sl[half]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinderV2:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        heappush(self.large, -heappushpop(self.small, -num))
        if len(self.large) > len(self.small):
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(-self.small[0])
