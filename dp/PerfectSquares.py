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
