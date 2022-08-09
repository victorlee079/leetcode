class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        n = len(arr)
        dp = [1] * n
        d = {x : i for i, x in enumerate(arr)}
        for i in range(n):
            for j in range(i):
                # arr[i] is divisible by arr[j]
                # r * arr[j] = arr[i]
                if arr[i] % arr[j] == 0:
                    r = arr[i] // arr[j]
                    if r in d:
                        dp[i] += dp[j] * dp[d[r]]
                        dp[i] %= MOD
        return sum(dp) % MOD
                
