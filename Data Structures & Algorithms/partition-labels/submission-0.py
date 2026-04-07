class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={}
        res=[]
        for i,e in enumerate(s):
            hashmap[e]=i
        start=0
        end=0    
        for i,e in enumerate(s):
            end=max(end,hashmap[e])
            if i==end:
                res.append(end-start+1)
                start=i+1
        return res        



