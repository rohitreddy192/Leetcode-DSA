
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty, d):

        n = len(jobDifficulty)

        if n < d:
            return -1

        @lru_cache(None)
        def dfs(i, days):

            # All jobs completed
            if i == n and days == 0:
                return 0

            # Invalid scheduling
            if i == n or days == 0:
                return float('inf')

            # Last day: all remaining jobs
            if days == 1:
                return max(jobDifficulty[i:])

            ans = float('inf')
            current_max = 0

            # Choose jobs for current day
            for j in range(i, n - days + 1):

                current_max = max(
                    current_max,
                    jobDifficulty[j]
                )

                remaining = dfs(j + 1, days - 1)

                ans = min(
                    ans,
                    current_max + remaining
                )

            return ans

        return dfs(0, d)
