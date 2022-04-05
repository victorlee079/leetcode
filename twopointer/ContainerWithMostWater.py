class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        vol = 0
        while l < r:
            vol = max((r - l) * min(height[r], height[l]), vol)
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1
        return vol