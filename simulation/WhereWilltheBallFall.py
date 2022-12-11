class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = set([(a, a) for a in range(n)])
        for i in range(m):
            new_dp = set()
            for k, j in dp:
                if grid[i][j] == 1 and j < n-1 and grid[i][j+1] != -1:
                    new_dp.add((k, j+1))
                elif grid[i][j] == -1 and j > 0 and grid[i][j-1] != 1:
                    new_dp.add((k, j-1))
            dp = new_dp
            if len(dp) < 1:
                return [-1] * n

        ret = [-1] * n
        for k, j in dp:
            ret[k] = j
        return ret

    # Botton Up DP
    def findBallDp(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m+1)]
        for i in range(m, -1, -1):
            for j in range(n):
                if i == m:
                    dp[i][j] = j
                    continue

                next_column = j + grid[i][j]
                if next_column < 0 or next_column > n-1 or grid[i][j] != grid[i][next_column]:
                    dp[i][j] = -1
                else:
                    dp[i][j] = dp[i+1][next_column]
        
        return dp[0]
