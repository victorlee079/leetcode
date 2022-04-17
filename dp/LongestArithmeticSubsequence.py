class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp, n = {}, len(nums)
        for i in range(1, n):
            for j in range(i):
                diff = nums[j] - nums[i]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2
        return max(dp.values())