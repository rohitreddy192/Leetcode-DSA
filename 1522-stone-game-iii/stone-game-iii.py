class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        @cache
        def solve(idx):

            if idx >= n:
                return 0

            ans = float("-inf")
            taken = 0

            for i in range(3):

                if idx + i >= n:
                    break

                taken += stoneValue[idx + i]

                ans = max(
                    ans,
                    taken - solve(idx + i + 1)
                )

            return ans

        ans = solve(0)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"