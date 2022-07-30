class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        queue = deque([])
        ans = deque([])
        cnt = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == "-":
                continue
            
            queue.appendleft(s[i].upper())
            cnt += 1
            if cnt == k:
                ans.appendleft("".join(queue))
                queue.clear()
                cnt = 0
        
        if queue:
            ans.appendleft("".join(queue))
        
        return '-'.join(ans)
