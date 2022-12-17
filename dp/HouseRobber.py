class Solution:
    # Always rob
    def rob(self, nums):
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp = [0] * n
        a, b, c = nums[0], max(nums[0], nums[1]), nums[0] + nums[2]
        
        for i in range(3, n):
            a, b, c = b, c, nums[i] + max(a, b)

        return max(a, b, c)
        
    # Rob or not rob
    def rob2(self, nums):
        rob, not_rob, n = 0, 0, len(nums)
        for i in range(n):
            # Rob this house implies we cannot rob the previous one
            # Not rob this house just store the max from previous
            rob, not_rob = not_rob + nums[i], max(rob, not_rob)
        return max(rob, not_rob)
        
