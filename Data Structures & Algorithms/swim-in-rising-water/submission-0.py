class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[(grid[0][0],0,0)]
        res=0
        n=len(grid)
        visited=set()
        direc=[(-1,0),(0,-1),(1,0),(0,1)]
        while heap:
            l,x,y=heapq.heappop(heap)
            visited.add((x,y))
            res = max(res,l)
            if (x,y)==(n-1,n-1):
                return res
                
            for dx,dy in direc:
                if 0<=x+dx<n and 0<=y+dy<n and (x+dx,y+dy) not in visited:
                                       
                    heapq.heappush(heap,(grid[x+dx][y+dy],x+dx,y+dy))
        return res            

