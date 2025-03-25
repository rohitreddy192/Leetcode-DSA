from typing import List, Tuple
from collections import deque

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        unique_islands = set()
        
        # Directions for DFS traversal (up, down, left, right)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # DFS to explore an island and store its shape
        def dfs(x: int, y: int) -> List[Tuple[int, int]]:
            stack = [(x, y)]
            island = []
            while stack:
                i, j = stack.pop()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                island.append((i, j))
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) not in visited:
                        stack.append((ni, nj))
            return island

        # Normalize an island shape by computing all rotations and reflections
        def normalize(shape: List[Tuple[int, int]]) -> Tuple:
            """
            Normalize the shape by computing all possible transformations.
            Each island shape can be transformed in 8 different ways:
            - 4 Rotations (0°, 90°, 180°, 270°)
            - 4 Reflections (left-right flip + each rotation)
            """
            shapes = []
            # Get all transformations (4 rotations, 4 reflections)
            for _ in range(2):  # One for normal, one for reflection
                new_shape = [(x, y) for x, y in shape]
                for _ in range(4):  # Rotate 4 times
                    new_shape = [(y, -x) for x, y in new_shape]  # Rotate 90° clockwise
                    min_x = min(p[0] for p in new_shape)
                    min_y = min(p[1] for p in new_shape)
                    normalized = sorted((x - min_x, y - min_y) for x, y in new_shape)
                    shapes.append(tuple(normalized))
                # Reflect across y-axis
                shape = [(-x, y) for x, y in shape]

            return min(shapes)  # Choose the lexicographically smallest one
        
        # Main loop to find islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island = dfs(i, j)  # Get raw island shape
                    normalized_shape = normalize(island)  # Normalize it
                    unique_islands.add(normalized_shape)

        return len(unique_islands)
