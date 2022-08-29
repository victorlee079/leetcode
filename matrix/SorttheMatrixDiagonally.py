class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        arr = [[] for _ in range(m+n-1)]
        
        def sortDiag(r, c, k):
            x, y = r, c
            while x < m and y < n:
                arr[k].append(mat[x][y])
                x += 1
                y += 1
            arr[k].sort()
            x, y, j = r, c, 0
            while x < m and y < n:
                mat[x][y] = arr[k][j]
                x += 1
                y += 1
                j += 1
        
        k = 0
        for i in range(m):
            sortDiag(i, 0, k)
            k += 1
            
        for i in range(1, n):
            sortDiag(0, i, k)
            k += 1
        
        return mat
