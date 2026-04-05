class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=[]
        def bck(op,cl):
            if op==n and cl==n:
                res.append("".join(path))
                return
            if op<n:
                path.append("(")
                bck(op+1,cl)
                path.pop()
            if cl<op:
                path.append(")")
                bck(op,cl+1)
                path.pop()
        bck(0,0)        
        return res

