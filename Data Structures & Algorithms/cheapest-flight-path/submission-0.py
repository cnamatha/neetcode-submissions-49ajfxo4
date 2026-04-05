class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,c in flights:
            graph[u].append((v,c))
        heap=[(0,src,0)]
        while heap:
            c1,u1,k1=heapq.heappop(heap)
            if k1>k+1:
                continue
            if u1==dst:
                return c1
            for v1,c2 in graph[u1]:
                heapq.heappush(heap,(c2+c1,v1,k1+1))
        return -1            