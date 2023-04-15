class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i-1]
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for coins in range(0, k + 1):
                for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                    current_sum = piles[i - 1][current_coins -
                                               1] if current_coins > 0 else 0
                    dp[i][coins] = max(dp[i][coins],
                                       dp[i - 1][coins - current_coins] + current_sum)
        return dp[n][k]
