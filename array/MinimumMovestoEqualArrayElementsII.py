class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2
        median = nums[mid]
        if n % 2 == 0:
            median = (nums[mid] + nums[mid-1]) // 2
        ans = 0
        for i in nums:
            ans += abs(median - i)
        return ans
     
    # O(n log n)
    # C is an element in the numbers between min and max
    # nums[n-1] - C + nums[n-2] - c + ... + C - nums[1] + C - nums[0]
    def minMoves2NoMed(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        ans = 0
        while l < r:
            ans += nums[r] - nums[l]
            l += 1
            r -= 1
        return ans
