class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_str(s):
            stk = []
            for c in s:
                if c == "#":
                    if stk:
                        stk.pop()
                else:
                    stk.append(c)
            return "".join(stk)

        return get_str(s) == get_str(t)
