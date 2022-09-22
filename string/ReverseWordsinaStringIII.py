class Solution:
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
