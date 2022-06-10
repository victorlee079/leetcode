class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        while l < r:
            while l < n and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            
            if l < r:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        
        return True
