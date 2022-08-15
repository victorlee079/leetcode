class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [(beginWord, 1)]

        wordSet = set(wordList)

        def bfs(q):
            while q:
                word, level = q.pop(0)
                if word == endWord:
                    return level
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nword = word[:i] + c + word[i + 1:]
                        if nword in wordSet:
                            q.append((nword, level + 1))
                            wordSet.remove(nword)
            return 0

        return bfs(q)
   
    def ladderLengthRevision(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([(beginWord, 1)])
        while q:
            word, cnt = q.popleft()
            if word == endWord:
                return cnt
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(97+j) + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, cnt+1))
        return 0
        
