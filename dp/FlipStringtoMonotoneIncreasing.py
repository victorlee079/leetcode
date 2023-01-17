class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zero = one = 0
        for i in range(n):
            flipOne = 1 if s[i] == "0" else 0
            if i == 0:
                zero, one = zero + (1 - flipOne), one + flipOne
            else:
                zero, one = zero + \
                    (1 - flipOne), min(zero + flipOne, one + flipOne)
        return min(one, zero)
