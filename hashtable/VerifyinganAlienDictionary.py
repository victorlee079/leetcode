class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = defaultdict(int)
        for i in range(len(order)):
            d[order[i]] = i
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            same = True
            for a, b in zip(word1, word2):
                if d[b] > d[a]:
                    same = False
                    break
                if d[a] > d[b]:
                    return False
            if same and len(word1) > len(word2):
                return False
        return True
