class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        forward = {}
        backward = {}
        for a, b in zip(words, pattern):
            if a in forward and forward[a] != b:
                return False
            if b in backward and backward[b] != a:
                return False
            forward[a] = b
            backward[b] = a
        return True
