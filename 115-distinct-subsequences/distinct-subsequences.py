class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = {}
        def solve(i,j):
            if j<0: return 1
            if i<0 and j>=0: return 0

            if (i,j) in dp: return dp[(i,j)]
            pick = solve(i-1,j-1) if i>=0 and j>=0 and s[i]==t[j] else 0
            not_pick = solve(i-1,j)

            dp[(i,j)] = pick + not_pick
            return dp[(i,j)]

        return solve(len(s)-1, len(t)-1)