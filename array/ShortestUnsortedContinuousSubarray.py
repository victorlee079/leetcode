class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        low, high = len(nums)-1, 0
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                low = min(low, i)
                high = max(high, i)
        return high - low + 1 if high - low > 0 else 0
