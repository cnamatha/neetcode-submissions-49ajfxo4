class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map={}
        i=0
        while i<len(nums):
            if nums[i] in nums_map:
                return True
            nums_map[nums[i]]=i
            i+=1
        return False        

