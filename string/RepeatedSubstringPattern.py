'''
Proof

Let P be the pattern
H = P without first char
T = P without last char

s = n * P
s[1:] = H + (n-1) * P
s[:-1] = (n-1) * P + T
s[1:] + s[:-1] = H + 2(n-1) * P + T
Then s is inside s[1:] + s[:-1]

'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_fold = "".join( (s[1:], s[:-1]) )
        return s in s_fold
