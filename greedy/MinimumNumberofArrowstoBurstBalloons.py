class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda p: p[0])
        ans = 1
        start, end = points[0]
        for i in range(1, len(points)):
            p = points[i]
            if p[0] <= end and p[1] >= start:
                start, end = max(p[0], start), min(p[1], end)
            else:
                start, end = p
                ans += 1
        return ans
