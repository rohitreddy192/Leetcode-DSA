class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for interval in intervals[1:]:
            if end>=interval[0]:
                end = max(end,interval[1])
            else:
                res.append([start,end])
                start, end = interval
        res.append([start,end])
        return res