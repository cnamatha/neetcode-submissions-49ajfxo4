class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digtochar={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}    
        res=[]
        path=[]
        def bck(i):
            if i==len(digits):
                res.append("".join(path))
                return
            for ch in digtochar[digits[i]]:
                path.append(ch)
                bck(i+1)
                path.pop()
        bck(0)        
        return res        


