class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        slow = -1
        ans = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                slow = -1
            else:
                if slow == -1:
                    slow = fast
                ans += fast - slow + 1
        return ans
