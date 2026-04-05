class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        max_freq=0
        left=0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            max_freq=max(max_freq,count[s[i]])
            if (i-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            res=max(res,(i-left+1))
        return res          
