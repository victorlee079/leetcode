class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                l, r = 0, n-1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
            elif target < row[0]:
                break
                
        return False
