class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return 0  

            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            cost1 = costs[0] + solve(j)

            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            cost7 = costs[1] + solve(j)

            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            cost30 = costs[2] + solve(j)

            return min(cost1, cost7, cost30)

        return solve(0)