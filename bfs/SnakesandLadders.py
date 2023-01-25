class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        last = n * n
        moves = 0
        q = deque([0])
        while q:
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                if curr == last - 1:
                    return moves
                for j in range(curr + 1, min(curr + 6 + 1, last)):
                    r, c = n - 1 - j // n, j % n
                    if j // n % 2 != 0:
                        c = n - 1 - c
                    if board[r][c] != -2:
                        if board[r][c] == -1:
                            q.append(j)
                        else:
                            q.append(board[r][c]-1)
                        board[r][c] = -2
            moves += 1
        return -1
