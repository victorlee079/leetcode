class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        fstCap = 65 <= ord(word[0]) <= 90
        upper = False
        for i in range(1, len(word)):
            if i == 1:
                upper = 65 <= ord(word[i]) <= 90
                if not fstCap and upper:
                    return False
            else:
                if not upper and 65 <= ord(word[i]) <= 90:
                    return False
                if upper and 97 <= ord(word[i]) <= 122:
                    return False

        return True
