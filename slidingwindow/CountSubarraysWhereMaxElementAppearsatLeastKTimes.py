class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        cnt = 0
        ans = 0
        l = 0
        for r in range(n):
            if nums[r] == m:
                cnt += 1
            while cnt == k:
                ans += n - r
                if nums[l] == m:
                    cnt -= 1
                l += 1
        return ans
                
            
