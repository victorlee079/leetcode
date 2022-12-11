class Solution:
    # Time O(n*k)
    # Space O(n*(2k+1))
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        for i in range(1, 2*k+1, 2):
            dp[0][i] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            for j in range(1, 2*k+1):
                sign = -1 if j % 2 == 1 else 1
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + sign * prices[i])
        return dp[-1][2*k]
        