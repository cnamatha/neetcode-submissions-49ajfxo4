class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        def pal(l,r):
            nonlocal count
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        for i in range(len(s)):
            pal(i,i)
            pal(i,i+1)
        return count                 