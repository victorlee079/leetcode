class Solution:
    def partitionString(self, s: str) -> int:
        mem = set()
        ans = 1
        slow = 0
        for i in range(len(s)):
            c = s[i]
            if c in mem:
                ans += 1
                slow = i
                mem.clear()
            mem.add(c)
        return ans
