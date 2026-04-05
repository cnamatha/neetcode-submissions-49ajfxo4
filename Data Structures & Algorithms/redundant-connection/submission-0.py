class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)
        res=[]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]    
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False
            if rank[px]>rank[py]:
                parent[py]=px
                
            elif rank[px]<rank[py]:
                parent[px]=py
                
            else:
                parent[py]=px
                rank[px]+=1
            return True    
        for x,y in edges:
            if not union(x,y):
                res=[x,y]
        return res        

