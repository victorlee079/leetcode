class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i, ans, cnt = 0, "", 1
        while i < len(s):
            l, r = i, min(i+k, len(s))
            if cnt % 2 != 0:
                ans = ans + s[l:r][::-1]
            else:
                ans = ans + s[l:r]
            i += k
            cnt += 1
        return ans
