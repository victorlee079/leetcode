class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = set([0, 1, 2, 5, 6, 8, 9])
        ng = set([0, 1, 8])
        ret = 0
        for i in range(n+1):
            s = set([int(j) for j in str(i)])
            if s.issubset(valid) and not s.issubset(ng):
                ret += 1
        return ret
