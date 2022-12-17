class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                else:
                    if i > 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        return dp[-1][-1]
