class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        res=[]
        col=set()
        posdia=set()
        nedia=set()
        def bck(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in posdia or (r-c) in nedia:
                    continue
                col.add(c)
                posdia.add(r+c)
                nedia.add(r-c)
                board[r][c]="Q"
                bck(r+1)
                col.remove(c)
                posdia.remove(r+c)
                nedia.remove(r-c)
                board[r][c]="."
        bck(0)        
        return res        
