class Solution:
    def firstUniqChar(self, s: str) -> int:
        mem = [0] * 26
        for i in range(len(s)):
            index = ord('a') - ord(s[i])
            mem[index] += 1
        for i in range(len(s)):
            index = ord('a') - ord(s[i])
            if mem[index] == 1:
                return i
        return -1
