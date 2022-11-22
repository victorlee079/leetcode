class Solution:
    def numSquaresRecurMem(self, n: int) -> int:
        mem = {}

        def recurion(n):
            if n == 0:
                return 0
            if n in mem:
                return mem[n]
            ret = math.inf
            for i in range(1, n+1):
                sq = i * i
                if sq > n:
                    break
                ret = min(ret, 1 + recurion(n - sq))
            mem[n] = ret
            return ret

        return recurion(n)
    # TLE
    def numSquares(self, n: int) -> int:
        mem = {}
        dp = [0] * (n+1)

        for i in range(1, n+1):
            ret = math.inf
            for j in range(1, i+1):
                sq = j * j
                if sq > i:
                    break
                ret = min(ret, 1 + dp[i - sq])
            dp[i] = ret
        return dp[n]
