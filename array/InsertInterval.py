class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        n = len(intervals)
        
        left, right = [], []
        for i in range(n):
            s, e = intervals[i]
            if e < start:
                left.append(intervals[i])
            elif s > end:
                right.append(intervals[i])
            else:
                start = min(s, start)
                end = max(e, end)

        
        return left + [[start, end]] + right
