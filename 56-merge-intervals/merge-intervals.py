class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<=end:
                end = max(end, intervals[i][1])
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]

        res.append([start,end])

        return res
