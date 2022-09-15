class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        ans = []
        tbr = defaultdict(int)
        changed.sort()
        
        for i in range(n-1, -1, -1):
            val = changed[i]
            if tbr[val] > 0:
                ans.append(val)
                tbr[val] -= 1
            elif val % 2 == 0:
                half = changed[i] // 2
                tbr[half] += 1
            else:
                return []
        
        return ans if all(v == 0 for v in tbr.values()) else []
