class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(x):
            s=0
            while x>0:
                k=x%10
                x=x//10
                s+=k*k
            
            return s

        h_set=set()
        s_n=n
        while s_n not in h_set and s_n!=1:
            h_set.add(s_n)
            s_n=helper(s_n)
            
       
        return s_n==1        

