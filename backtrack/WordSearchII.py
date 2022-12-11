class Solution:
    def findWords(self, board, words):
        class TrieNode:
            def __init__(self, char):
                self.char = char
                self.is_end = False
                self.children = {}
                self.cnt = 0

        trie = TrieNode("")
        m, n = len(board), len(board[0])
        for word in words:
            ct = trie
            for c in word:
                if c not in ct.children:
                    ct.children[c] = TrieNode(c)
                ct = ct.children[c]
                ct.cnt += 1
            ct.is_end = True

        ret = []
        dir = [0, 1, 0, -1, 0]

        def remove(trie, word):
            for c in word:
                trie = trie.children[c]
                trie.cnt -= 1

        def dfs(r, c, t, v, path):
            curr = board[r][c]

            if curr not in t.children:
                return
            nt = t.children[curr]
            # No need to search
            if nt.cnt < 1:
                return
            if nt.is_end:
                w = "".join(path)
                ret.append(w)
                # Prune path
                remove(trie, w)
                # Remove searched word
                nt.is_end = False

            for i in range(4):
                nr, nc = r+dir[i], c+dir[i+1]
                if -1 < nr < m and -1 < nc < n and (nr, nc) not in v:
                    v.add((nr, nc))
                    path.append(board[nr][nc])
                    dfs(nr, nc, nt, v, path)
                    v.remove((nr, nc))
                    path.pop()

        for i in range(m):
            for j in range(n):
                visited = set()
                visited.add((i, j))
                dfs(i, j, trie, visited, [board[i][j]])

        return ret
