class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, ret = len(s), []

        def backtrack(path, index):
            if len(path) == 4:
                if index == len(s):
                    ret.append(".".join(path))
                return

            for i in range(index+1, min(index+4, n+1)):
                seg = s[index:i]
                if len(seg) > 1 and seg[0] == "0":
                    continue
                if int(seg) <= 255:
                    path.append(seg)
                    backtrack(path, i)
                    path.pop()

        backtrack([], 0)
        return ret
