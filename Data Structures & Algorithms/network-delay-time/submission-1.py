class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))
        dist={}
        heap=[]
        heapq.heappush(heap,(0,k))
        while heap:
            w,n1=heapq.heappop(heap)
            if n1 in dist:
                continue
            dist[n1]=w    
            for d,nei in graph[n1]:
                if nei not in dist:
                    heapq.heappush(heap,(d+w,nei))
        if len(dist)!=n:
            return -1
        return max(dist.values())                        