class Solution:
    def rob(self, nums):
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp = [0] * n
        a, b, c = nums[0], max(nums[0], nums[1]), nums[0] + nums[2]

        for i in range(3, n):
            a, b, c = b, c, nums[i] + max(a, b)

        return max(a, b, c)
        
