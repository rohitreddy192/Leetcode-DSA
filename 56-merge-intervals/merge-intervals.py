class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        res = list()
        if len(intervals) == 0: return [[]]
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals:
            if i[0]<=end:
                end = max(end,i[1])
            else:
                res.append([start,end])
                start = i[0]
                end = i[1]
        res.append([start,end])
        return res