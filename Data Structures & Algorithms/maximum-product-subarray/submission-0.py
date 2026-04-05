class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=nums[0]    
        currMax=1
        currMin=1
        for n in nums:
            if n<0:
                currMax,currMin=currMin,currMax
            currMax=max(n,currMax*n)
            currMin=min(n,currMin*n)
            res=max(res,currMax)
        return res        
