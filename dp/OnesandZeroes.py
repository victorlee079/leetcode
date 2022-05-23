class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            z = o = 0
            overflow = False
            for c in s:
                if c == "1":
                    o += 1
                else:
                    z += 1
                if z > m or n > n:
                    overflow = True
                    break
            if overflow:
                continue
            for i in range(m, z-1, -1):
                for j in range(n, o-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-z][j-o]+1)
        return dp[-1][-1]
