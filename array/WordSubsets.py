class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def getMask(word):
            mask = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                mask[i] += 1
            return mask

        max_bm = [0] * 26
        for b in words2:
            bm = getMask(b)
            for j in range(26):
                max_bm[j] = max(max_bm[j], bm[j])

        ans = []
        for a in words1:
            am = getMask(a)
            subset = True
            for j in range(26):
                if am[j] < max_bm[j]:
                    subset = False
                    break
            if subset:
                ans.append(a)

        return ans
