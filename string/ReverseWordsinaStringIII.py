class Solution:
    # Stack
    def reverseWords(self, s: str) -> str:
        stk = []
        ans = []
        for c in s:
            if c == " ":
                while stk:
                    ans.append(stk.pop())
                ans.append(c)
            else:                    
                stk.append(c)
        while stk:
            ans.append(stk.pop())
        return "".join(ans)
    
    # Two pointer
    def reverseWords2p(self, s: str) -> str:
        n = len(s)
        ans = list(s)
        space = -1
        for i in range(n+1):
            if i == n or s[i] == " ":
                start = space + 1
                end = i - 1
                while start < end:
                    ans[start], ans[end] = s[end], s[start]
                    start += 1
                    end -= 1
                space = i
        return "".join(ans)
