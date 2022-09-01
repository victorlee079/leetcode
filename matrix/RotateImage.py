class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(mat)
        # Number of cycles
        n = m+1 if m%2==1 else m
        
        for i in range(n//2):
            # Skip the last one for each cycle
            # m-i-1 is the width of a cycle
            for j in range(i, m-i-1):
                mat[i][j], mat[j][m-i-1], mat[m-i-1][m-j-1], mat[m-j-1][i] = mat[m-j-1][i], mat[i][j], mat[j][m-i-1], mat[m-i-1][m-j-1]
