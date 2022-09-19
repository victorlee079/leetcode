class Solution:
    # O(w*n^2)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            l, r = 0, len(word)-1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans = []
        
        # Word to index mapping
        d = {word : i for i, word in enumerate(words)}
        
        for j, word in enumerate(words):
            n = len(word)
            for i in range(n+1):
                pre = word[:i]
                suf = word[i:]
                if is_palindrome(pre):
                    rev = suf[::-1]
                    if rev != word and rev in d:
                        ans.append([d[rev], j])
                if i != n and is_palindrome(suf):
                    rev = pre[::-1]
                    if rev in d:
                        ans.append([j, d[rev]])
                        
        return ans
