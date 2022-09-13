class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        h = []
        res = sSum = 0
        # Sort by efficiency in descending order
        # Use heapq to keep track the largest k elements
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                # Pop the engineer with smallest speed
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7)
