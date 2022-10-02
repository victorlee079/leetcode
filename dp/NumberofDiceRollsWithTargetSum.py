class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for a in range(target+1)] for b in range(n)]

        # first dice
        for i in range(1, min(k+1, target+1)):
            dp[0][i] = 1

        # remaining dice
        for i in range(1, n):
            for j in range(target, 0, -1):
                for p in range(1, k+1):
                    if j-p > -1:
                        dp[i][j] += dp[i-1][j-p]
        return dp[-1][-1] % 1000000007

        