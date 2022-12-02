class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        if count1.keys() != count2.keys():
            return False
            
        chars1 = count1.most_common()
        chars2 = count2.most_common()
        for a, b in zip(chars1, chars2):
            if a[1] != b[1]:
                return False

        return True
