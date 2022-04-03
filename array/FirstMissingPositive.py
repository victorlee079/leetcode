from math import inf


class Solution:

    def firstMissingPositive(self, nums):
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = 0

        for i, num in enumerate(nums):
            index = abs(num) - 1
            if 0 <= index < len(nums):
                if nums[index] == 0:
                    nums[index] = -inf
                elif nums[index] > 0:
                    nums[index] = -nums[index]
        for index, num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1


s = Solution()
ans = s.firstMissingPositive([-1, 4, 2, 1, 9, 10])
print(ans)
