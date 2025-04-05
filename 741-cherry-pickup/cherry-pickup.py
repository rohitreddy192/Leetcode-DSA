class Solution:
    def cherryPickup(self,grid):
        N = len(grid)
        
        @lru_cache(None)
        def dp(r1, c1, r2, c2):
            # If out of bounds or on a thorn (-1), return a very low value
            if r1 >= N or c1 >= N or r2 >= N or c2 >= N or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            # If both persons reach the bottom-right cell
            if r1 == N - 1 and c1 == N - 1 and r2 == N-1 and c2==N-1:
                return grid[r1][c1]
            
            # Collect cherries, ensuring no double counting
            cherries = grid[r1][c1] if (r1, c1) == (r2, c2) else grid[r1][c1] + grid[r2][c2]
            
            # Move in all possible directions
            cherries += max(
                dp(r1 + 1, c1, r2 + 1, c2),  # Both move down
                dp(r1 + 1, c1, r2, c2 + 1),  # P1 moves down, P2 moves right
                dp(r1, c1 + 1, r2 + 1, c2),  # P1 moves right, P2 moves down
                dp(r1, c1 + 1, r2, c2 + 1)   # Both move right
            )
            
            return cherries
        
        return max(0, dp(0, 0, 0, 0))
