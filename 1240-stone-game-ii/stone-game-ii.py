class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        @cache
        def solve(idx, isAlice, M):

            if idx >= n:
                return 0

            ans = 0 if isAlice else float("inf")
            taken = 0

            for X in range(1, 2 * M + 1):

                if idx + X > n:
                    break

                taken += piles[idx + X - 1]

                newM = max(M, X)

                if isAlice:
                    # Alice takes these stones
                    ans = max(
                        ans,
                        taken + solve(idx + X, False, newM)
                    )
                else:
                    # Bob takes these stones
                    # They don't add to Alice's score
                    ans = min(
                        ans,
                        solve(idx + X, True, newM)
                    )

            return ans

        return solve(0, True, 1)

# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         M = 1

#         @cache
#         def solve(idx, isAlice, M):
#             if idx == n:
#                 return 0

#             pick_for_alice = 0
#             for i in range(1,M*2+1,1):
#                 if isAlice:
#                     sum(piles[idx:idx+i]) + solve(idx+i, not isAlice, i)
