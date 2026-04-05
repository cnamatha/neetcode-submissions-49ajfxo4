class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def bck(start,path):
            res.append(path[:])
                      
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                bck(i+1,path)
                path.pop()
        bck(0,[])
        return res