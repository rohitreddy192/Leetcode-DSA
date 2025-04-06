from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        # Step 1: Build the graph: val -> list of indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        # Step 2: BFS setup
        visited = [False] * n
        queue = deque()
        queue.append((0, 0))  # (index, steps)
        visited[0] = True

        while queue:
            index, steps = queue.popleft()

            # Check if we reached the last index
            if index == n - 1:
                return steps

            # Step 3: Add neighbors
            for nei in [index - 1, index + 1]:
                if 0 <= nei < n and not visited[nei]:
                    visited[nei] = True
                    queue.append((nei, steps + 1))

            # Step 4: Same-value jump
            for nei in graph[arr[index]]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append((nei, steps + 1))

            # Optional but important: clear to avoid redundant jumps
            graph[arr[index]] = []

        return -1  # should never happen
