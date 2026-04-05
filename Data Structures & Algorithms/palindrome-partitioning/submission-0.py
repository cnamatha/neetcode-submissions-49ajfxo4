class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def isPal(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def bck(k):
            if k==len(s):
                res.append(path[:])
                return
            for l in range(k,len(s)):
                if isPal(k,l):
                    path.append(s[k:l+1])
                    bck(l+1)
                    path.pop()
        bck(0)
        return res
