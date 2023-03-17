class TrieNode:
    def __init__(self, ch):
        self.d = {}
        self.ch = ch
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in curr.d:
                curr.d[ch] = TrieNode(ch)
            curr = curr.d[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in curr.d:
                return False
            curr = curr.d[ch]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            ch = prefix[i]
            if ch not in curr.d:
                return False
            curr = curr.d[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
