class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stk, second = [], -math.inf
        for i in range(n-1, -1, -1):
            if nums[i] < second:
                return True
            while stk and nums[i] > stk[-1]:
                second = stk.pop()
            stk.append(nums[i])
        return False