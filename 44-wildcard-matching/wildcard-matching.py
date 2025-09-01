class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        @cache
        def solve(i,j):
            if i>=n:
                while j<m and p[j]=="*":
                    j += 1
                return j>=m
            if j>=m: return i>=n

            if i<n and j<m and (s[i]==p[j] or p[j]=="?"):
                return solve(i+1,j+1)
            elif p[j]=="*":
                return solve(i+1,j) or solve(i,j+1)
            
            return False
        
        return solve(0,0)