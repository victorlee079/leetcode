class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        adj = [0, 1, 0, -1, 0]

        if m * n < len(word):
            return False
        if not Counter(word) <= Counter(chain(*board)):
            return False

        def dfs(r, c, step):
            if board[r][c] == word[step]:
                if step == len(word)-1:
                    return True
                temp, board[r][c] = board[r][c], '#'
                for i in range(4):
                    nr, nc = r+adj[i], c+adj[i+1]
                    if -1 < nr < m and -1 < nc < n and board[nr][nc] != '#':
                        if dfs(nr, nc, step+1):
                            return True
                board[r][c] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
