class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]
        rows=len(board)
        cols=len(board[0])
        root={}
        for word in words:
            node=root
            for ch in word:
                node=node.setdefault(ch,{})
            node["#"]=word
        def bck(r,c,node):
            ch=board[r][c]
            if ch not in node:
                return
            nxt=node[ch]
            if "#" in nxt:
                res.append(nxt["#"])
                del nxt["#"]
            board[r][c]="#"    
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                k,l=r+dr,c+dc
                if 0<=k<rows and 0<=l<cols and board[k][l]!="#":
                    bck(k,l,nxt)
            board[r][c]=ch
            if not nxt:
                node.pop(ch)
        for i in range(rows):
            for j in range(cols):
                bck(i,j,root)        
        return res


                      