'''
Good to Know

You need to know the difference between subarray and subsequence.
Subarray need to be consecutive。
Subsequence don't have to be consecutive.

Intuition

If it's empty sting, return 0;
If it's palindrome, return 1;
Otherwise, we need at least 2 operation.

Explanation

We can delete all characters 'a' in the 1st operation,
and then all characters 'b' in the 2nd operation.
So return 2 in this case

Complexity

Time O(N)
Space O(N), also O(1) space checking palindrome is suuggested.
'''

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        if s:
            return 1 if isPalindrome(s) else 2
        else:
            return 0
