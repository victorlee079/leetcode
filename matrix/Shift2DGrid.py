class Solution:
    def shiftGrid(self, grid, k):
        vec = []
        nc = len(grid[0])
        for i in range(len(grid)):
            vec += grid[i]
        
        n = len(vec)
        k %= n
        vec = vec[-k:] + vec[:-k]
        ans = []
        for i in range(len(grid)):
            ans.append(vec[i*nc:i*nc+nc])
        return ans
