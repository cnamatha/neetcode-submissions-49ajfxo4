class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        seen_set=set()
        max_length=0
        for right in range(len(s)):
            while s[right] in seen_set:
                seen_set.remove(s[start])
                start+=1
            seen_set.add(s[right])    
            max_length=max(max_length,right-start+1)
        return max_length            

