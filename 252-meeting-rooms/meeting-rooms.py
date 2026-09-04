class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Step 1: Sort intervals by start time
        intervals.sort()

        # Step 2: Check for overlap
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:  # Current start < previous end
                return False

        return True