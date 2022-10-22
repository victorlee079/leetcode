from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        dt = Counter(t)
        win = n
        while win <= m:
            for i in range(m-win+1):
                ds = Counter()
                for j in range(i, i+win):
                    if s[j] in dt:
                        ds[s[j]] += 1
                ds.subtract(dt)
                ret = True
                for k, v in ds.items():
                    if v < 0:
                        ret = False
                if ret:
                    return s[i:i+win]
            win += 1
        return ""

    def minWindowON(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        dt = defaultdict(int)
        for c in t:
            dt[c] += 1

        start, end, minStart, minLen, counter = 0, 0, 0, math.inf, n
        while end < m:
            c1 = s[end]
            if dt[c1] > 0:
                counter -= 1
            dt[c1] -= 1
            end += 1
            while counter == 0:
                if minLen > end - start:
                    minLen = end - start
                    minStart = start
                c2 = s[start]
                dt[c2] += 1
                if dt[c2] > 0:
                    counter += 1
                start += 1
        if minLen == math.inf:
            return ""
        else:
            return s[minStart:minStart + minLen]
