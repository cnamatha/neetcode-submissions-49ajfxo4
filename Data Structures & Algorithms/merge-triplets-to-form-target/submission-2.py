class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        m=len(triplets)
        goos=set()
        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0]:
                goos.add(0)
            if b==target[1]:
                goos.add(1)
            if c==target[2]:
                goos.add(2)        
            
        return len(goos)==3        
