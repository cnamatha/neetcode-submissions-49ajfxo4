class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=2,1
        for i in range(n-1):
            a,b=a+b,a
        return b    

