d = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

class Solution:
    def romanToInt(self, s):
        res, n, prev = 0, len(s), 0

        for i in range(n-1, -1, -1):
            minus = False
            if prev > d[s[i]]:
                minus = True
            prev = val = d[s[i]]
            if minus:
                res -= val
            else:
                res += val
        return res
