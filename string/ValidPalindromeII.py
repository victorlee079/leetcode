class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        n, deleted = len(s), False
        l, r = 0, n-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s, l+1, r) or isPalindrome(s, l, r-1)
        return True
