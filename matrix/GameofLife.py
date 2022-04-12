class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def countNeighbors(board, i, j):
            cnt = 0
            drt = [-1, 0, 1, 0, -1, -1, 1, 1, -1]
            for k in range(len(drt)-1):
                if 0 <= i+drt[k] < m and 0 <= j+drt[k+1] < n and (1 <= abs(board[i+drt[k]][j+drt[k+1]]) <= 3):
                    cnt += 1
            return cnt

        for i in range(m):
            for j in range(n):
                lives = countNeighbors(board, i, j)
                if board[i][j] == 1:
                    if lives < 2:
                        board[i][j] = -1 # Case 1 (died in next round)
                    elif lives > 3:
                        board[i][j] = -3 # Case 3 (died in next round)
                else:
                    if lives == 3:
                        board[i][j] = -4
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -4:
                    board[i][j] = 1
                elif board[i][j] == -1 or board[i][j] == -3:
                    board[i][j] = 0
                        
                
