from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 1: Find connected components and check bipartiteness
        color = {}  # To store colors (0 or 1)
        components = []  # List to store all connected components

        def bfs_check(start):
            queue = deque([start])
            component = set()
            color[start] = 0  # Start coloring
            while queue:
                node = queue.popleft()
                component.add(node)
                for neighbor in adj[node]:
                    if neighbor in color:
                        if color[neighbor] == color[node]:  # Odd cycle detected
                            return None
                    else:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
            return component

        visited = set()
        for node in range(1, n + 1):
            if node not in visited:
                component = bfs_check(node)
                if component is None:  # Odd cycle found
                    return -1
                visited.update(component)
                components.append(component)

        # Step 2: Find max groups for each component using BFS
        def bfs_depth(start):
            queue = deque([(start, 1)])  # (node, depth)
            visited = set([start])
            max_depth = 1
            while queue:
                node, depth = queue.popleft()
                max_depth = max(max_depth, depth)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))
            return max_depth

        # Sum up max depth for each connected component
        return sum(max(bfs_depth(node) for node in comp) for comp in components)
