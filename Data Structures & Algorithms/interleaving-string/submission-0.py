class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo={}
        def dfs(i,j,turn):
            if (i,j,turn) in memo:
                return memo[(i,j,turn)]
            k=i+j
            if k==len(s3):
                return i==len(s1) and j==len(s2)
            if turn==0:
                for l in range(1,len(s1)-i+1):
                    if s1[i:i+l]==s3[k:k+l] and dfs(i+l,j,1):
                        memo[(i,j,turn)]=True
                        return True
            else:
                for l in range(1,len(s2)-j+1):
                    if s2[j:j+l]==s3[k:k+l] and dfs(i,j+l,0):
                        memo[(i,j,turn)]=True
                        return True
            memo[(i,j,turn)]=False                        
            return False
        return dfs(0,0,0) or dfs(0,0,1)    