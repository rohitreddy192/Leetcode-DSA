class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        @lru_cache(None)
        def solve(i,j):
            if i>=n and j>=m: return 1
            if i>=n: return 0
            
            not_pick = solve(i+1,j)
            pick = 0
            if i<n and j<m and s[i]==t[j]:
                pick = solve(i+1,j+1)

            return pick + not_pick

        return solve(0,0)