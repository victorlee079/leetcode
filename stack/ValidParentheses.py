class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in d:
                if not stk or stk[-1] != d[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk
