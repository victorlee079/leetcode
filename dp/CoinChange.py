class Solution:
    def coinChange(self, coins, amount):

        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(1 + dp[i-c], dp[i])

        return dp[amount] if dp[amount] != math.inf else -1
        
