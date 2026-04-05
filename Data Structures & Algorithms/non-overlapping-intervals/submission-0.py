class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        prev_end=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prev_end:
                prev_end=end
            else:
                prev_end=min(end,prev_end)
                count+=1
        return count            