class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mini=min(nums)
        maxi=max(nums)
        res=[0]*n
        range_n=maxi-mini+1
        count=[0]*range_n
        for num in nums:
            count[num-mini]+=1
        for i in range(1,range_n):
            count[i]+=count[i-1]
        for j in range(n-1,-1,-1):
            num=nums[j]
            count[num-mini]-=1
            res[count[num-mini]]=num
        return res            