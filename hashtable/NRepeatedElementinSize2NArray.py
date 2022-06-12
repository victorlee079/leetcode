class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n, d = len(nums)//2, defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] == n:
                return num
        return None
