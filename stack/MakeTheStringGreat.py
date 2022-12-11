class Solution:
    def makeGood(self, s: str) -> str:
        stk = []

        def sameChar(a, b):
            return ord(a) - ord('a') == ord(b) - ord('A') or ord(a) - ord('A') == ord(b) - ord('a')

        for c in s:
            if stk and sameChar(stk[-1], c):
                stk.pop()
            else:
                stk.append(c)
        
        return "".join(stk)
