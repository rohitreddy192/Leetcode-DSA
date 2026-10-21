
from functools import cache
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)

        @cache
        def solve(idx):
            if idx >= n:
                return 0

            start, end, gain = jobs[idx]

            next_idx = bisect_left(starts, end)

            pick = gain + solve(next_idx)
            not_pick = solve(idx + 1)

            return max(pick, not_pick)

        return solve(0)
