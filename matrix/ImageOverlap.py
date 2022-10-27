class Solution:
    # Convolution (TLE)
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ret = 0

        ones = []
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    ones.append((i, j))

        def convolute(offsetX, offsetY):
            cnt = 0
            for _, (i, j) in enumerate(ones):
                if -1 < i + offsetX < n and -1 < j + offsetY < n:
                    cnt += 1 if img2[i][j] == img1[i+offsetX][j+offsetY]  else 0
            return cnt

        for i in range(-(n-1), n):
            for j in range(-(n-1), n):
                res = convolute(i, j)
                ret = max(ret, res)
        
        return ret
    
    # Numpy
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps
