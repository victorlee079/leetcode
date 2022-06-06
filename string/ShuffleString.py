class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ret = [None] * n
        for i, v in enumerate(indices):
            ret[v] = s[i]
        return "".join(ret)