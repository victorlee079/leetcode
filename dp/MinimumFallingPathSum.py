class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                min_val = matrix[i-1][j]
                if j > 0:
                    min_val = min(min_val, matrix[i-1][j-1])
                if j < n-1:
                    min_val = min(min_val, matrix[i-1][j+1])
                matrix[i][j] += min_val
        return min(matrix[-1])
