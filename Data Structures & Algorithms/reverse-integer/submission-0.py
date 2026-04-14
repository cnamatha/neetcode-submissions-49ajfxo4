class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX=(2**31)-1
        res=0
        sign=1
        if x<0:
            sign=-1
            x=abs(x)
        while x:
            pop=x%10
            x//=10
            if res>(INT_MAX-pop)//10:
                return 0
            res=res*10+pop
        return res*sign        