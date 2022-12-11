class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        prefix_sums = [0] * n
        for i in range(n):
            if i == 0:
                prefix_sums[i] = nums[i]
            else:
                prefix_sums[i] = prefix_sums[i-1] + nums[i]
        ans, min_diff = -1, math.inf
        for i in range(n):
            a = prefix_sums[i] // (i+1)
            b = (prefix_sums[n-1] - prefix_sums[i]
                 ) // (n-i-1) if n - i - 1 != 0 else 0
            diff = abs(a - b)
            if diff < min_diff:
                min_diff, ans = diff, i
        return ans
