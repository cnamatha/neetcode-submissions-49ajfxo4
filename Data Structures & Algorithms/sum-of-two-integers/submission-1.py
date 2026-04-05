class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        mask_int=0x7FFFFFFF
        while b!=0:
            carry=(a&b)&mask
            a=(a^b)&mask
            b=(carry<<1)&mask
        return a if a<mask_int else ~(a^mask)    
            