class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = pow(2, k)
        found = set()
        
        for i in range(k, len(s)+1):
            ss = s[i-k:i]
            if ss not in found:
                found.add(ss)
                cnt -= 1
                if cnt == 0:
                    return True
        return False
