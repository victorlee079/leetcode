# Time complexity is O(n*s) + O(n^2), where s is the average length of word and n is number of words. Space complexity is O(n).
class Solution:
    def maxProduct(self, words):
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans
