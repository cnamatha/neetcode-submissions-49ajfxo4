class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        heap=[(0,0)]
        visited=set()
        count=0
        while heap:
            d,u=heapq.heappop(heap)
            if u in visited:
                continue
            count+=d
            visited.add(u)
            x1,y1=points[u]
            for j in range(n):
                if j not in visited:
                    x2,y2=points[j]
                    dist=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,(dist,j))
        return count            
