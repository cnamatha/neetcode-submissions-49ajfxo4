class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        INF=2147483647
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            r,c=q.popleft()
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==INF:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))
                                     
