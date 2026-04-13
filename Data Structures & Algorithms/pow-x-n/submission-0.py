class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        k=self.myPow(x,n//2)        
        if n%2==0:
                
            return k*k
        return k*k*x            