
from functools import cache
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)

        @cache
        def solve(i):
            if i == n:
                return 0

            # Skip current job
            not_pick = solve(i + 1)

            # Pick current job
            next_idx = bisect_left(starts, jobs[i][1])
            pick = jobs[i][2] + solve(next_idx)

            return max(pick, not_pick)

        return solve(0)
