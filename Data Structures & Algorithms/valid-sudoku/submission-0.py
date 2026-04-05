class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m=len(board)
        n=len(board[0])
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] not in rows[i] and board[i][j] not in cols[j] and board[i][j] not in box[3*(i//3)+(j//3)]):
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    box[3*(i//3)+(j//3)].add(board[i][j])
                else:
                    return False
        return True                
