# O(n)
class Solution:
    def sortedSquares(self, nums):
        l, r = 0, len(nums)-1
        ret, i = [0]*len(nums), len(nums)-1
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                ret[i] = nums[l] ** 2
                l += 1
            else:
                ret[i] = nums[r] ** 2
                r -= 1
            i -= 1
        return ret
