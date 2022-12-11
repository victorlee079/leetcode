from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        items = sorted(s.items(), key=lambda e: e[1], reverse=True)
        ans = []
        for k, v in items:
            for i in range(v):
                ans.append(k)
        return "".join(ans)
