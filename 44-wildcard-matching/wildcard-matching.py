class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n, m = len(s), len(p)

        @cache
        def solve(i, j):

            # Both strings completely processed
            if i < 0 and j < 0:
                return True

            # Pattern exhausted but string remains
            if j < 0:
                return False

            # String exhausted
            if i < 0:
                # Remaining pattern must be all '*'
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True

            # '?' matches exactly one character
            if p[j] == '?':
                return solve(i - 1, j - 1)

            # '*' matches:
            # 1. zero characters
            # 2. one or more characters
            if p[j] == '*':
                return solve(i, j - 1) or solve(i - 1, j)

            # Normal character
            if s[i] == p[j]:
                return solve(i - 1, j - 1)

            return False

        return solve(n - 1, m - 1)