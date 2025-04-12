class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = SortedList()
        for time in timePoints:
            new_time_list = time.split(":")
            times.add(int(new_time_list[0])*60 + int(new_time_list[1]))
        
        minDiff = 1e9

        print(times)
        for timeIdx in range(len(times)-1):
            new_diff = times[timeIdx+1]-times[timeIdx]
            minDiff = min(minDiff, new_diff )
        
        return min(minDiff, 24*60 - times[-1] + times[0])