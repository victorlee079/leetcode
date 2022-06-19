class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j    # Min. operations = j
                elif j == 0:
                    dp[i][j] = i    # Min. operations = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Delete from word1, word2 or both
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[m][n]
