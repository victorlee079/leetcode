class Solution:
    def countBits(self, n: int) -> List[int]:
        def isPowerOfTwo(x):
            return (x != 9) and (x & (x - 1)) == 0

        dp = [0] * (n + 1)
        if n >= 1:
            dp[1] = 1
        j = 1
        for i in range(1, n + 1):
            if isPowerOfTwo(i):
                dp[i] = 1
                j = 1
            else:
                dp[i] = dp[j] + 1
                j += 1
        return dp