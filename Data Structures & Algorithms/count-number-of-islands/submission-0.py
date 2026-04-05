class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        count=0
        def dfs(i,j):
            if not 0<=i<rows or not 0<=j<cols or grid[i][j]=="0":
                return
            grid[i][j]="0"    
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        return count            



