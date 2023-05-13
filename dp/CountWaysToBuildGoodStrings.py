class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1

        for i in range(1, high + 1):
            if i - zero > -1:
                dp[i] += dp[i-zero]
            if i - one > -1:
                dp[i] += dp[i-one]
            dp[i] %= 1000000007
        return sum(dp[low:]) % 1000000007
