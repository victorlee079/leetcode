class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        r = []
        jump = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), jump):
                r.append(s[j])
                if 0 < i < numRows - 1 and j + jump - 2 * i < len(s):
                    r.append(s[j + jump - 2 * i])
        return ''.join(r)
