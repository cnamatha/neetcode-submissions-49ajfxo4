class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        top, bottom=0,m-1
        while top<=bottom:
            mid1=(top+bottom)//2
            if matrix[mid1][n-1]<target:
                top=mid1+1
            elif matrix[mid1][0]>target:
                bottom=mid1-1
            else:
                break

        if not(top<=bottom):
            return False
        row=(top+bottom)//2

        right,left=n-1,0
        while left<=right:
            mid2=(right+left)//2
            if matrix[row][mid2]==target:
                return True
            elif matrix[row][mid2]>target:
                right=mid2-1
            else:
                left=mid2+1
        return False                                    

                     