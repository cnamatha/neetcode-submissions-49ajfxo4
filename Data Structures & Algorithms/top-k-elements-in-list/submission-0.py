class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        bucket=[[] for _ in range(len(nums)+1)]
        res=[]
        for i,c in count.items():
            bucket[c].append(i)
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
# Counter have .items(), .keys, .values, .get(key);cannot[key], .most_common(k)