class Solution:
    def uniquePaths2D(self, m, n):
      grid = [[1 for j in range(n)] for i in range(m)]
      for i in range(m):
          for j in range(n):
              if i > 0 and j > 0:
                  grid[i][j] = grid[i-1][j] + grid[i][j-1]
      return grid[-1][-1]
  
    def uniquePaths1D(self, m, n):
        grid = [1 for j in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                grid[j] = grid[j] + grid[j-1]
        return grid[-1]
