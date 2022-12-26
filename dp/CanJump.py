class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lp = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= lp:
                lp = i
        return lp == 0