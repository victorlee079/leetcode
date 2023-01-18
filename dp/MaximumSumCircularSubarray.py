class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        curr_min, global_min = 0, math.inf
        curr_max, global_max = 0, -math.inf
        total = 0
        for i in range(n):
            total += nums[i]

            curr_min = min(nums[i], curr_min + nums[i])
            global_min = min(global_min, curr_min)

            curr_max = max(nums[i], curr_max + nums[i])
            global_max = max(global_max, curr_max)

        # All negative
        if total == global_min:
            return global_max
        return max(global_max, total - global_min)
