class Solution:
    def trap(self, height):
        ans = 0
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        lmax[0] = height[0]
        rmax[-1] = height[-1]
        for j in range(1, n):
            lmax[j] = max(lmax[j-1], height[j])
        for j in range(n-2, -1, -1):
            rmax[j] = max(rmax[j+1], height[j])
        for i in range(n):        
            ans += min(lmax[i], rmax[i]) - height[i]
        return ans
