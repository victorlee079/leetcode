class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = defaultdict(int)
        words = set(words)
        for word in words:
            morse = []
            for c in word:
                i = ord(c) - ord('a')
                morse.append(codes[i])
            d["".join(morse)] += 1
        return len(d)
