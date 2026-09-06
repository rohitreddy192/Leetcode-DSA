class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @cache
        def solve(n, alice_turn):

            if n == 0:
                return not alice_turn

            if alice_turn:
                # Alice wants to find ONE move where she wins
                for i in range(1, int(n ** 0.5) + 1):

                    if solve(n - i * i, False):
                        return True

                return False

            else:
                # Bob wants to find ONE move where Alice loses
                for i in range(1, int(n ** 0.5) + 1):

                    if not solve(n - i * i, True):
                        return False

                return True

        return solve(n, True)