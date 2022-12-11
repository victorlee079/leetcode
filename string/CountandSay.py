class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = self.countAndSay(n-1)
        currC, cnt = "", 0
        ans = []
        for c in res:
            if c != currC:
                if cnt > 0:
                    ans.append(str(cnt) + currC)
                currC, cnt = c, 1
            else:
                cnt += 1
        if cnt > 0:
            ans.append(str(cnt) + currC)
        return "".join(ans)
