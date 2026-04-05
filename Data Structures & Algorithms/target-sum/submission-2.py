class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums)+target)%2!=0 or target>sum(nums):
            return 0
        P=(sum(nums)+target)//2
        dp=[0]*(P+1)
        dp[0]=1
        for num in nums:
            for i in range(P,num-1,-1):
                dp[i]+=dp[i-num]
        return dp[P]            