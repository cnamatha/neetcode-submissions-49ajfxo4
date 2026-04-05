class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_count=0
        for num in nums:
            
            if num-1 not in num_set:
                current=num
                count=1
                while current+1 in num_set:
                    count+=1
                    current+=1
                max_count=max(count,max_count)
        return max_count            


