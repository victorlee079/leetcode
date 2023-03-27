class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]
