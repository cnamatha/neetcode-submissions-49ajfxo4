class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        stack=[]
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                res=max(res,width*height)
            stack.append(i)
        return res                
