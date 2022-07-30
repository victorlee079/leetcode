class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def getMask(word):
            mask, d, cnt = [0] * len(word), {}, 1
            for i in range(len(word)):
                c, ind = word[i], cnt
                if c in d:
                    ind = d[c]
                else:
                    d[c] = cnt
                    cnt += 1
                mask[i] = ind
            return mask
    
        mask = getMask(pattern)
        res = []
        for word in words:
            if len(word) == len(pattern) and mask == getMask(word):
                res.append(word)
        
        return res

    def findAndReplacePattern2Map(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            if len(word) != len(pattern):
                return False
            
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if m1[w] != p or m2[p] != w:
                    return False
            return True
        
        return filter(match, words)
            
        
            
        
