class Solution:
    def longestPalindrome(self, s):
      start = end = 0
      maxWidth = 0
      for i in range(len(s)):
        odd = expandAroundCenter(s, i, i)
        even = expandAroundCenter(s, i, i + 1)
        w = max(odd, even)
        if w > maxWidth:
          #
          start = i - (w - 1) // 2
          end = i + w // 2
          maxWidth = w
      return s[start:end+1]

def expandAroundCenter(s, left, right):
  l = left
  r = right
  while l >= 0 and r < len(s) and s[l] == s[r]:
    l -= 1
    r += 1
  return r - l - 1
