class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        n, m = len(text), len(pattern)

        @cache
        def solve(i,j):
            if j==m: return i==n
            is_match = i<n and (text[i]==pattern[j] or pattern[j]==".")

            if j<m-1 and pattern[j+1]=="*":
                return (is_match and solve(i+1,j)) or solve(i, j+2)
            else:
                return is_match and solve(i+1,j+1)
            
        return solve(0,0)