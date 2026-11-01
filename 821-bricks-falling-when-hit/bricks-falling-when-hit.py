
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]


class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])

        # Virtual roof node
        roof = m * n

        dsu = DSU(m * n + 1)

        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]

        def get_id(r, c):
            return r * n + c

        # Step 1: Apply all hits upfront
        valid = []

        for r, c in hits:
            if grid[r][c] == 1:
                valid.append(True)
                grid[r][c] = 0
            else:
                valid.append(False)

        # Step 2: Construct DSU using remaining bricks
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                curr = get_id(r, c)

                # Connect top-row bricks to virtual roof
                if r == 0:
                    dsu.union(curr, roof)

                # Connect right and bottom neighbors
                for dr, dc in [(1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 1):

                        dsu.union(curr, get_id(nr, nc))

        # Step 3: Restore hits in reverse order
        result = [0] * len(hits)

        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]

            # Nothing was removed at this position
            if not valid[i]:
                continue

            # Roof component size before restoration
            old_size = dsu.size[dsu.find(roof)]

            # Restore the brick
            grid[r][c] = 1
            curr = get_id(r, c)

            # Connect to roof if top row
            if r == 0:
                dsu.union(curr, roof)

            # Connect to all active neighboring bricks
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    grid[nr][nc] == 1):

                    dsu.union(curr, get_id(nr, nc))

            # Roof component size after restoration
            new_size = dsu.size[dsu.find(roof)]

            # Exclude the brick we just restored
            result[i] = max(0, new_size - old_size - 1)

        return result
