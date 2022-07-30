class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0 for c in range(n)] for r in range(m)]
        dp[startRow][startColumn] = 1
        modulo = 1000000000 + 7
        
        ans = 0
        for i in range(maxMove):
            next_dp = [[0 for c in range(n)] for r in range(m)]
            
            for j in range(m):
                for k in range(n):
                    # Add
                    if j == m-1:
                        ans = (ans + dp[j][k]) % modulo
                    if j == 0:
                        ans = (ans + dp[j][k]) % modulo
                    if k == n-1:
                        ans = (ans + dp[j][k]) % modulo
                    if k == 0:
                        ans = (ans + dp[j][k]) % modulo
                    
                    # Update
                    if j > 0:
                        next_dp[j-1][k] += dp[j][k]
                    if j < m-1:
                        next_dp[j+1][k] += dp[j][k]
                    if k > 0:
                        next_dp[j][k-1] += dp[j][k]
                    if k < n-1:
                        next_dp[j][k+1] += dp[j][k]
            dp = next_dp
            
        return ans % modulo
