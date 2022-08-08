class Solution:
    def countVowelPermutation(self, n: int) -> int:
        nv = 5
        dp = [[1] * nv for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % 1000000007
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 1000000007
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % 1000000007
            dp[i][3] = (dp[i - 1][2]) % 1000000007
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000007

        return sum(dp[-1]) % 1000000007

    def countVowelPermutationLessMem(self, n: int) -> int:
        a = e = i = o = u = 1

        for _ in range(1, n):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        return (a + e + i + o + u) % 1000000007
