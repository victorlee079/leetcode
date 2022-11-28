class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        ans = 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                # Continuous
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans
    
    def numberOfArithmeticSlicesLessSpace(self, nums: List[int]) -> int:
        curr, prev = 0, 0
        ans = 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                curr = prev + 1
            else:
                curr = 0
            ans += curr
            prev = curr
        return ans
