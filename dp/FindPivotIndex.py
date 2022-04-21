class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = nums[i - 1] + dp[i - 1]
        for i in range(n):
            if dp[i] == dp[-1] - dp[i + 1]:
                return i
        return -1
