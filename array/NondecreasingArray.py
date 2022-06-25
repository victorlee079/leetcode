class Solution:
    def checkPossibility(self, nums):
        def checkIncreasing(nums):
            a = nums[0]
            for b in range(1, len(nums)):
                if a > nums[b]:
                    return False
                a = nums[b]
            return True

        n = len(nums)
        prev = nums[0]
        for i in range(1, n):
            if prev > nums[i]:
                if i >= 2:
                    return checkIncreasing(nums[i-2:i-1] + nums[i:]) or checkIncreasing(nums[i-2:i] + nums[i+1:])
                else:
                    return checkIncreasing(nums[i:])
            prev = nums[i]

        return True

s = Solution()
print(s.checkPossibility([4,3,4,3]))
