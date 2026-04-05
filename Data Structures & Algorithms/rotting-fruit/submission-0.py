class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1    
        t=0            
        while q and fresh:
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                    if 0<=dx<m and 0<=dy<n and grid[dx][dy]==1:
                        q.append((dx,dy))
                        grid[dx][dy]=2
                        fresh-=1
            t+=1
        
        return t if fresh==0 else -1                       

        