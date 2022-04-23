class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        for item in counts.items():
            if item[1] == 1:
                ans += item[0]
        return ans