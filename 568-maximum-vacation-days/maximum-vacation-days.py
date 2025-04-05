class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:        
        N = len(flights)      # number of cities
        K = len(days[0])      # number of weeks
        
        @lru_cache(maxsize=None)
        def solve(city, week):
            if week == K:
                return 0

            max_vac = 0

            for dest in range(N):
                if flights[city][dest] == 1 or city == dest:  # can fly or stay
                    vacation_days = days[dest][week] + solve(dest, week + 1)
                    max_vac = max(max_vac, vacation_days)

            return max_vac

        return solve(0, 0)
