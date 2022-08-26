class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened, stk = 0, []
        
        for c in s:
            if c == "(":
                if opened >= 1:
                    stk.append(c)
                opened += 1
            else:
                if opened > 1:
                    stk.append(c)
                opened -= 1
        
        return "".join(stk)
