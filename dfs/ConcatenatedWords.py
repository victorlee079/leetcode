class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Faster access
        words = set(words)
        mem = {}

        def dfs(word):
            if word in mem:
                return mem[word]
            mem[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words and suffix in words:
                    mem[word] = True
                    return True
                if prefix in words and dfs(suffix):
                    mem[word] = True
                    return True
                if dfs(prefix) and suffix in words:
                    mem[word] = True
                    return True
            return False

        ans = []
        for w in words:
            if dfs(w):
                ans.append(w)

        return ans


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def search(self, word):
        node = self.root

        def dfs(node, word, index):
            if index == len(word):
                return True

            for i in range(index, len(word)):
                c = word[i]
                if c in node.children:
                    node = node.children[c]
                    if node.is_end and dfs(self.root, word, i+1):
                        return True
                else:
                    return False

            return False

        return dfs(node, word, 0)


class SolutionWithTrieAndDFS:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        words = sorted(words, key=lambda w: len(w))
        ans = []
        for word in words:
            if trie.search(word):
                ans.append(word)
            else:
                trie.insert(word)
        return ans
