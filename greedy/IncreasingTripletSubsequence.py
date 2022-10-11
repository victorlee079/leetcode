class Solution:
    def increasingTripletDp(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        dp = [1] * n
        for i in range(1, n):
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] == 3:
                        return True

        return False
        
