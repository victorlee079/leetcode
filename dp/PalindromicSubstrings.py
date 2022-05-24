class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ret = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                if i == j or (s[i] == s[j] and (dp[i+1][j-1] or j-i == 1)):
                    dp[i][j] = True
                if dp[i][j] == True:
                    ret += 1
        return ret
