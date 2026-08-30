class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def solve(i, j):
            if i == j:
                return piles[i]

            return max(
                piles[i] - solve(i + 1, j),
                piles[j] - solve(i, j - 1)
            )

        return solve(0, len(piles) - 1) > 0