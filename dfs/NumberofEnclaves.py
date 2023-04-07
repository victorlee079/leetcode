class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        ans = 0

        def dfs(i, j):
            grid[i][j] = -1
            di = [0, 1, 0, -1, 0]
            for k in range(4):
                if -1 < i+di[k] < n and -1 < j+di[k+1] < m and grid[i+di[k]][j+di[k+1]] == 1:
                    dfs(i+di[k], j+di[k+1])

        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][m-1] == 1:
                dfs(i, m-1)
        for j in range(m):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[n-1][j] == 1:
                dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 1

        return ans
