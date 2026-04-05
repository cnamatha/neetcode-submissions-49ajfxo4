class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        total=m+n
        half=(m+n)//2
        left,right=0,m
        while True:
            i=(left+right)//2
            j=half-i
            A1=nums1[i-1] if i>0 else float("-inf")
            A2=nums1[i] if i<m else float("+inf")
            B1=nums2[j-1] if j>0 else float("-inf")
            B2=nums2[j] if j<n else float("-inf")
            if A1<=B2 and B1<=A2:
                if total%2:
                    return min(A2,B2)
                else:
                    return (max(A1,B1)+min(A2,B2))/2
            elif A1>B2:
                right=i-1
            else:
                left=i+1                  

        