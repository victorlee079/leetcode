# O(n)
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        # Cannot break the palindrome if only 1 character        
        if n == 1:
            return ""

        # If any of the characters in the first half is not 'a', just replace by 'a'
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        # If the palindrome contains 'a' only, replace the last character by 'b'
        return palindrome[:n-1] + "b"
