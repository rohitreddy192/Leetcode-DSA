class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def solve(i,j):
            if j<0: return 1
            if i<0 and j>=0: return 0

            pick = solve(i-1,j-1) if i>=0 and j>=0 and s[i]==t[j] else 0
            not_pick = solve(i-1,j)
            return pick + not_pick

        return solve(len(s)-1, len(t)-1)