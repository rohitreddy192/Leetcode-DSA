class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        n, m = len(text), len(pattern)

        @cache
        def solve(i, j):
            if j == m:
                return i == n

            first_match = i < n and (text[i] == pattern[j] or pattern[j] == ".")

            if j+1 < m and pattern[j+1] == "*":
                # zero occurrence OR one occurrence if first matches
                return solve(i, j+2) or (first_match and solve(i+1, j))
            else:
                return first_match and solve(i+1, j+1)

        return solve(0, 0)
