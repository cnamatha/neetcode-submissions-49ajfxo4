class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(start,path,net):
            if net==0:
                res.append(path[:])
                return
            if net<0:
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,path,net-nums[i])
                path.pop()
        backtrack(0,[],target)
        return res                 