class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        @cache
        def solve(i,j):
            if j<0: return 1
            if i<0: return j<0
            pick = 0
            if s[i]==t[j]:
                pick =  solve(i-1,j-1)

            
            not_pick = solve(i-1,j)
        
            return pick + not_pick
            
        return solve(n-1,m-1)
