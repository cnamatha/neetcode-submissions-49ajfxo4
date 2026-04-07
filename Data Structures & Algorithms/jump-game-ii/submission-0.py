class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        max_possible=0
        current_end=0
        for i in range(len(nums)-1):
            max_possible=max(i+nums[i],max_possible)
            if i==current_end:
                jumps+=1
                current_end=max_possible
        return jumps    
