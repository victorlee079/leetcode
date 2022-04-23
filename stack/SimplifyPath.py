class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for c in path.split("/"):
            if not c or c == ".":
                continue
            elif c == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(c)

        return "/" + "/".join(stk)