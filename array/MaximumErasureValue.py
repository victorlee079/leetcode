class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d, n = {}, len(nums)
        cum = [0] * n
        l = score = 0
        highest = 0
        for r in range(n):
            if r > 0:
                cum[r] = cum[r - 1] + nums[r]
            else:
                cum[r] = nums[r]

            if nums[r] in d and d[nums[r]] >= l:
                l = d[nums[r]] + 1

            if l > 0:
                score = cum[r] - cum[l - 1]
            else:
                score = cum[r]

            d[nums[r]] = r
            highest = max(highest, score)
        return highest