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

    # Cannot pass all test cases
    def maxPerformanceDp(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # dp[i][j] = max. performance 
        dp = [[(0, inf) for i in range(k+1)] for j in range(n)]
        ans = speed[0] * efficiency[0]
        
        for i in range(1, k+1):
            dp[0][i] = (speed[0], efficiency[0])
            
        for i in range(1, n):
            for j in range(1, k+1):
                speed_sum, min_eff = dp[i-1][j-1]
                old_perf = dp[i-1][j][0] * dp[i-1][j][1]
                new_perf = (speed_sum + speed[i]) * min(min_eff, efficiency[i])
                if new_perf > old_perf:
                    speed_sum += speed[i]
                    min_eff = min(min_eff, efficiency[i])
                    dp[i][j] = (speed_sum, min_eff)
                else:
                    dp[i][j] = dp[i-1][j]
                ans = max(ans, dp[i][j][0] * dp[i][j][1])

        return ans % (10**9 + 7)
