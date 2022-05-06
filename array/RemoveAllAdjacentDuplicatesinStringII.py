class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        
        for c in s:
            if stk:
                if c == stk[-1][0] :
                    if stk[-1][1] + 1 == k:
                        stk.pop()
                    else:
                        stk[-1] = (c, stk[-1][1]+1)
                else:
                    stk.append((c, 1))
            else:
                stk.append((c, 1))
        
        return "".join([s[0]*s[1] for s in stk])
