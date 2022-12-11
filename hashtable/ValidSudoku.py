class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in rows[i] or v in cols[j] or v in boxes[i//3*3 + j//3]:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                boxes[i//3*3 + j//3].add(v)
        return True
