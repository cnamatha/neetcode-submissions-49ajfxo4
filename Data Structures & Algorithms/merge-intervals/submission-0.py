class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res=[intervals[0]]
        for start,end in intervals[1:]:
            recent_end=res[-1][1]
            if start<=recent_end:
                res[-1][1]=max(end,recent_end)
            else:
                res.append([start,end])
        return res             

