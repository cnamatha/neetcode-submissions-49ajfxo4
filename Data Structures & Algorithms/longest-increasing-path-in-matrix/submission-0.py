class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m,n=len(matrix),len(matrix[0])
        memo=[[0]*n for _ in range(m)]

        def dfs(i,j):
            if memo[i][j]!=0:
                return memo[i][j] 
            dir=[(0,1),(0,-1),(-1,0),(1,0)]
            max_len=1
            for dx,dy in dir:
                if 0<=(i+dx)<m and 0<=(j+dy)<n and matrix[i+dx][j+dy]>matrix[i][j]:
                    max_len=max(max_len,1+dfs(i+dx,j+dy))
            memo[i][j]=max_len        
            return max_len
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,dfs(i,j))
        return res                     
