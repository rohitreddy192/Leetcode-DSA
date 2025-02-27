class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = {}
        n, m = len(text), len(pattern)
        def solve(i,j):
            if i>=n and j>=m: return True
            if j>=m: return False
            if (i,j) in dp: return dp[(i,j)]

            match = i<n and (text[i]==pattern[j] or pattern[j]==".")
            if j+1<m and pattern[j+1]=="*":
                dp[(i,j)] = (match and solve(i+1,j)) or solve(i,j+2)
                return dp[(i,j)]
            if match:
                dp[(i,j)] = solve(i+1,j+1)
                return dp[(i,j)]
            dp[(i,j)] = False
            return dp[(i,j)]
        return solve(0,0)
