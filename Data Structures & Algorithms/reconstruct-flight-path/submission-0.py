class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for u,v in sorted(tickets,reverse=True):
            graph[u].append(v)
        res=[]
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)
        dfs("JFK")    
        return res[::-1]    

