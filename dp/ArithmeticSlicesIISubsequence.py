class Solution:
    # O(n^2)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        cnt = defaultdict(dict)
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # cnt[j][diff] contains the count of delta
                s = cnt[j][diff] if diff in cnt[j] else 0
                if diff not in cnt[i]:
                    cnt[i][diff] = 0
                cnt[i][diff] += s + 1
                ans += s
        return ans
