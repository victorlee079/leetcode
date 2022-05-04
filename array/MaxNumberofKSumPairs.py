class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        ans = 0
        for i, v in d.items():
            if k - i == i:
                ans += d[i] // 2
                d[i] = 0
            elif k - i in d:
                ans += min(d[k-i], v)
                d[i] = d[k-i] = 0
        return ans
      
    def maxOperationsWithNoExtraSpace(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        
        ans = 0
        while l < r:
            if nums[l] + nums[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return ans
