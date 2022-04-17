class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row, col = {}, {}
        ans = 0
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if r not in row:
                    row[r] = max(grid[r])
                if c not in col:
                    highest = 0
                    for i in range(n):
                        highest = max(highest, grid[i][c])
                    col[c] = highest
                ans += min(row[r], col[c]) - grid[r][c]
        return ans