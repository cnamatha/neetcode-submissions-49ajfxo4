class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        t=sum(nums)//2
        dp=[False]*(t+1)
        dp[0]=True
        for num in nums:
            for i in range(t,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
        return dp[t]             