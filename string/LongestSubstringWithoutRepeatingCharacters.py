# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, l, w = {}, 0, 0        
        for r in range(len(s)):
            if s[r] not in d:
                w = max(w, r - l + 1)
            else:
                # Window start position > repeated character's position
                if d[s[r]] < l:
                    w = max(w, r - l + 1)
                else:
                # Reset to last pos + 1
                    l = d[s[r]] + 1
            d[s[r]] = r
        return w
            
