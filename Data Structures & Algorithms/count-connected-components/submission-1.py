class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res=n
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                x=find(parent[x])
            return x
        def union(a,b):
            nonlocal res
            k,l=find(a),find(b)
            if k!=l:
                parent[l]=k
                res-=1
        for u,v in edges:
            union(u,v)
        return res                    