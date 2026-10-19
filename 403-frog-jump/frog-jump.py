
class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        stone_idx = {stone: i for i, stone in enumerate(stones)}
        dp = {}

        def solve(idx, jumpSize):
            if idx == n - 1:
                return True

            if (idx, jumpSize) in dp:
                return dp[(idx, jumpSize)]

            for jump in (jumpSize - 1, jumpSize, jumpSize + 1):
                if jump <= 0:
                    continue

                target = stones[idx] + jump

                if target in stone_idx:
                    if solve(stone_idx[target], jump):
                        dp[(idx, jumpSize)] = True
                        return True

            dp[(idx, jumpSize)] = False
            return False

        return solve(0, 0)
