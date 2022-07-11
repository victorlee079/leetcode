class Solution:
    # O(n*k) TLE
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            temp, nums[i] = nums[i], -math.inf
            for j in range(i-1, max(-1, i-k-1), -1):
                nums[i] = max(nums[i], temp + nums[j])
        return nums[-1]
