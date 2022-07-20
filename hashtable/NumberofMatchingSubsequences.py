class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            startingChar = word[0]
            buckets[startingChar].append(word)

        ans = 0
        for c in s:
            currBucket = buckets[c]
            buckets[c] = []
            for w in currBucket:
                if len(w) == 1:
                    ans += 1
                else:
                    startingChar = w[1]
                    buckets[startingChar].append(w[1:])
        return ans
