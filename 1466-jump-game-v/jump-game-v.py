from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            max_len = 1  # at least this node

            # Jump to the right
            for j in range(i+1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                max_len = max(max_len, 1 + dfs(j))

            # Jump to the left
            for j in range(i-1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                max_len = max(max_len, 1 + dfs(j))

            return max_len

        return max(dfs(i) for i in range(n))
