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
