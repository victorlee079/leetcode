class Solution:
    # TLE
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        
        if endWord not in wordList or beginWord == endWord:
            return []
        
        q = deque([(beginWord, 1, [beginWord])])
        res = []
        
        def bfs():
            while q:
                word, cnt, path = q.popleft()
                if word == endWord:
                    return path

                for i in range(len(word)):
                    for j in range(26):
                        newWord = word[:i] + chr(97+j) + word[i+1:]
                        if newWord in wordSet:
                            wordSet.remove(newWord)
                            newpath = path[::]
                            newpath.append(newWord)
                            q.append((newWord, cnt+1, newpath))
            return None
        
        path = bfs()
     
        def backtrack(path, wordSet, targetLen, word, endWord):
            if len(path) > targetLen:
                return
            if word == endWord:
                res.append(path[::])
                return
            
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(97+j) + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        path.append(newWord)
                        backtrack(path, wordSet, targetLen, newWord, endWord)
                        path.pop()
                        wordSet.add(newWord)
                    
        if path:
            n = len(path)
            backtrack([beginWord], set(wordList), n, beginWord, endWord)
        
        return res
