class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        # Map stone position -> index
        mark = {stones[i]: i for i in range(n)}

        @lru_cache(None)
        def solve(index: int, prev_jump: int) -> bool:
            # If we reached the last stone
            if index == n - 1:
                return True

            # Try jumps: k-1, k, k+1
            for next_jump in (prev_jump - 1, prev_jump, prev_jump + 1):
                if next_jump > 0:
                    next_pos = stones[index] + next_jump
                    if next_pos in mark:
                        if solve(mark[next_pos], next_jump):
                            return True

            return False

        # Start from index 0 with previous jump = 0 
        return solve(0,0)