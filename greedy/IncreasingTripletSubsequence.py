class Solution:
    # TLE O(n^2)
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
    
    # O(n)
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Current min 1st and current min 2nd
        first = second = inf
        for num in nums:
            # Found 1 number > current min 2nd
            if num > second:
                return True
            elif num > first:
                second = num
            elif num < first:
                first = num
        return False
        
