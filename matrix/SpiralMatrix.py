class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = [0, 1, 0, -1, 0]
        
        ans = []
        k = i = j = 0
        while i < len(matrix) and j < len(matrix[0]) and matrix[i][j] is not None:
                ans.append(matrix[i][j])
                matrix[i][j] = None
                if i + d[k] >= len(matrix) or j + d[k+1] >= len(matrix[0]) or matrix[i+d[k]][j+d[k+1]] is None:
                    if k == 3:
                        k = 0
                    else:
                        k += 1
                i += d[k]
                j += d[k+1]
        return ans
