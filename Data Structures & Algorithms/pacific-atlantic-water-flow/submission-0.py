class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()
        def dfs(i,j,reach):
            reach.add((i,j))
            for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                l,k=i+dr,j+dc
                if 0<=l<rows and 0<=k<cols and (l,k) not in reach and heights[l][k]>=heights[i][j]:
                    dfs(l,k,reach)
        for c in range(cols):
            dfs(0,c,pac)
            dfs(rows-1,c,atl)
        for r in range(rows):
            dfs(r,0,pac)
            dfs(r,cols-1,atl)
        return list(pac&atl)                    
