class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        d = defaultdict(int)
        
        # Horizontal
        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c-1]
        
        # For pair of two columns
        for i in range(n):
            for j in range(i, n):
                c = defaultdict(int)
                cur, c[0] = 0, 1
                for k in range(m):
                    # sum of cells from column i to j and row 0 to k
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    ans += c[cur - target]
                    c[cur] += 1
                    
        return ans
