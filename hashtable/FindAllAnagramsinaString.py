class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = [0] * 26
        n = len(p)
        for i in range(n):
            index = ord(p[i]) - ord('a')
            count[index] += 1

        ans = []
        match = [0] * 26
        for i in range(len(s)):
            if i >= n:
                dec = ord(s[i-n]) - ord('a')
                match[dec] -= 1
            inc = ord(s[i]) - ord('a')
            match[inc] += 1
            if match == count:
                ans.append(i-n+1)
        return ans
