from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Unique ID for each island (starting from 2)
        island_sizes = {0: 0}  # Dictionary to store island sizes

        def dfs(i, j, island_id):
            """DFS to compute island size and mark it with a unique ID."""
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = island_id  # Mark the cell with the island ID
            return 1 + sum(dfs(i + dx, j + dy, island_id) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])

        # Step 1: Assign unique IDs to each island and store their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1  # Move to next unique island ID

        # Step 2: Find the largest island if we flip a `0` to `1`
        max_island = max(island_sizes.values())  # Max existing island size
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_islands = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            unique_islands.add(grid[ni][nj])
                    new_size = 1 + sum(island_sizes[iid] for iid in unique_islands)
                    max_island = max(max_island, new_size)

        return max_island
