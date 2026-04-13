class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m=len(num1)
        n=len(num2)
        res=[0]*(m+n)
        num1=num1[::-1]
        num2=num2[::-1]

        for i in range(m):
            for j in range(n):
                res[i+j]+=(ord(num1[i])-ord("0"))*(ord(num2[j])-ord("0"))
                res[i+j+1]+=res[i+j]//10
                res[i+j]=res[i+j]%10
        while res and res[-1]==0:
            res.pop()
        return "".join(map(str,res[::-1]))            