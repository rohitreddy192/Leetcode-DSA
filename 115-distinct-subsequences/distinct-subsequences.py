class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def solve(i,j):
            if j<0: return 1
            if i<0: return 1 if j<0 else 0
            
            pick = 0
            if s[i]==t[j]:
                pick = solve(i-1,j-1)
            not_pick= solve(i-1,j)

            return pick+not_pick

        return solve(len(s)-1, len(t)-1)

