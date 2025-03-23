class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            
            # Extend same-colored segment to the left
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1
            
            # Option 1: Remove the k+1 group now
            max_points = (k + 1) * (k + 1) + dp(l + 1, r, 0)

            # Option 2: Try merging with other boxes of the same color
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    max_points = max(max_points, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))

            return max_points

        return dp(0, n - 1, 0)

