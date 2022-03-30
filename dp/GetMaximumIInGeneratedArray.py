class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp, m = [0] * (n+1), 0
        if n > 0:
            dp[1] = m = 1
        for i in range(2, n+1):
            if i % 2:
                dp[i] = dp[i//2] + dp[i//2+1]
            else:
                dp[i] = dp[i//2]
            m = max(m, dp[i])
        return m