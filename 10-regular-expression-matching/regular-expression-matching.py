class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        n, m = len(text), len(pattern)
        @lru_cache(None)
        def solve(i,j):
            if i>=n and j>=m: return True
            if j>=m: return False
            match = i<n and (text[i]==pattern[j] or pattern[j]==".")
            if j+1<m and pattern[j+1]=="*":
                return (match and solve(i+1,j)) or solve(i,j+2)
            if match:
                return solve(i+1,j+1)
            return False
        
        return solve(0,0)