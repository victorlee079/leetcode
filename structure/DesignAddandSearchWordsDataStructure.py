class TrieNode:

    def __init__(self, ch):
        self.ch = ch
        self.isEnd = False
        self.map = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.map:
                curr.map[c] = TrieNode(c)
            curr = curr.map[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, word, node):
            if index == len(word):
                if node.isEnd:
                    return True
                else:
                    return False
            c = word[index]
            if c != '.':
                if c not in node.map:
                    return False
                else:
                    if dfs(index+1, word, node.map[c]):
                        return True
            else:
                for k in node.map.keys():
                    if dfs(index+1, word, node.map[k]):
                        return True
            return False

        return dfs(0, word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
