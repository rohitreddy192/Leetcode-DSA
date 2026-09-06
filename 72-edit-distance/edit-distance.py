class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        dp = {}

        def solve(i, j):
            if j < 0:
                return i + 1

            if i < 0:
                return j + 1

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = solve(i - 1, j - 1)

            else:
                dp[(i, j)] = 1 + min(
                    solve(i - 1, j),       # delete
                    solve(i - 1, j - 1),   # replace
                    solve(i, j - 1)       # insert
                )

            return dp[(i, j)]

        return solve(n - 1, m - 1)