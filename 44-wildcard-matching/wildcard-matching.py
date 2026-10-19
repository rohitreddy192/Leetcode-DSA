from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def solve(i, j):
            if i < 0 and j < 0:
                return True

            if j < 0:
                return False

            if i < 0:
                return all(p[k] == '*' for k in range(j + 1))

            if p[j] == '?' or p[j] == s[i]:
                return solve(i - 1, j - 1)

            if p[j] == '*':
                return solve(i - 1, j) or solve(i, j - 1)

            return False

        return solve(len(s) - 1, len(p) - 1)