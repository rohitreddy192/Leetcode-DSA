class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def solve(n):
            if n<=2:
                return n
            return solve(n-2) + solve(n-1) 

        return solve(n)



















        # @lru_cache(maxsize=None)
        # def solve(ind):
        #     if ind==0: return 1
        #     if ind<0: return 0
        #     two_step = 0
        #     one_step = solve(ind-1)
        #     if ind>1:
        #         two_step = solve(ind-2)
        #     return one_step + two_step
        # return solve(n)