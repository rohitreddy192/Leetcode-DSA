class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @cache
        def solve(n, alice_turn):

            if n == 0:
                return not alice_turn

            for i in range(1, int(n ** 0.5) + 1):
                if alice_turn and solve(n - i*i, False):
                    return True
                if not alice_turn and not solve(n - i*i, True):
                    return False

            return not alice_turn

        return solve(n, True)