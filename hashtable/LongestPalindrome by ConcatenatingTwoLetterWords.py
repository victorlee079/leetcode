class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ret = 0
        words = Counter(words)
        plus2 = False

        for word, cnt in words.items():
            if cnt < 1:
                continue
            # Same character
            if word[0] == word[1]:
                if cnt % 2 == 0:
                    ret += cnt * 2
                else:
                    ret += (cnt-1)*2
                    plus2 = True
            else:
                rword = word[::-1]
                if rword in words and words[rword] > 0:
                    rcnt = words[rword]
                    occurrence = min(rcnt, cnt)
                    ret += occurrence * 4
                    words[word] -= occurrence
                    words[rword] -= occurrence

        return ret if not plus2 else ret + 2
