class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [0] * 26
        for c in sentence:
            letters[ord(c) - ord('a')] += 1
        for i in range(26):
            if letters[i] == 0:
                return False
        return True

    def checkIfPangramSet(self, sentence: str) -> bool:
        letters = set()
        for c in sentence:
            letters.add(c)
        return len(letters) == 26
