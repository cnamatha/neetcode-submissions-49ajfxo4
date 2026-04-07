class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_possible=0
        for i in range(len(nums)):
            if i>max_possible:
                return False
            max_possible=max(i+nums[i],max_possible)
        return True            
