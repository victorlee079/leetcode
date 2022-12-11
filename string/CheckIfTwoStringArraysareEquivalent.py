class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

    def arrayStringsAreEqualPointers(self, word1: List[str], word2: List[str]) -> bool:
        i = j = k = p = 0
        while i < len(word1) and j < len(word2):
            if word1[i][k] != word2[j][p]:
                return False
            k += 1
            p += 1
            if k == len(word1[i]):
                i += 1
                k = 0
            if p == len(word2[j]):
                j += 1
                p = 0

        return i == len(word1) and j == len(word2)
