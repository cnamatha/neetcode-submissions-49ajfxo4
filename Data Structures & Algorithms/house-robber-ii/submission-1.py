class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]    
        def max_rob(array_in):
            prev1=0
            prev2=0
            for i in range(len(array_in)):
                curr=max(prev1,prev2+array_in[i])
                prev2=prev1
                prev1=curr
            return prev1
        return max(max_rob(nums[:-1]),max_rob(nums[1:]))        