class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t=Counter(t)
        count_ss=Counter()
        need=len(count_t)
        have=0
        left=0
        res=""
        min_len=float("inf")
        for right in range(len(s)):
            c=s[right]
            count_ss[c]+=1
            if c in count_t and count_t[c]==count_ss[c]:
                have+=1
            while have==need:
                if right-left+1<min_len:
                    min_len=right-left+1
                    res=s[left:right+1]
                count_ss[s[left]]-=1
                if s[left] in count_t and count_ss[s[left]]<count_t[s[left]]:
                    have-=1
                left+=1
        return res            
