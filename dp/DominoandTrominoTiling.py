class Solution:
    def numTilings(self, n):
            dp = [0] * (1001)
            dp[0] = dp[1] = 1
            dp[2] = 2
            dp[3] = 5
            # Each dp[i] = dp[i-1] + dp[i-2] + 2 * (dp[i-3] + ... + dp[0])
            # dp[i-1] + dp[i-3] + dp[i-2] + dp[i-3] + 2 * (dp[i-4] + ... + dp[0])
            # 2 * dp[i-1] + dp[i-3]
            for i in range(4, n+1):
                dp[i] = 2 * dp[i-1] + dp[i-3]
            return dp[n] % 1000000007

s = Solution()
print(s.numTilings(3))