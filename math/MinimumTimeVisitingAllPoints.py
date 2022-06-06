class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calSteps(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return max(abs(x1 - x2), abs(y1 - y2))

        res, n = 0, len(points)
        for i in range(n - 1):
            a, b = points[i], points[i + 1]
            res += calSteps(a, b)
        return res