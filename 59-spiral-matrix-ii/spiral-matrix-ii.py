class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def dfs(cnt, mat, i, j, n, direction):
            mat[i][j] = cnt[0]  # Update the current cell
            cnt[0] += 1

            # Directions for right, down, left, up
            r = [0, 1, 0, -1]
            c = [1, 0, -1, 0]

            # Explore the current direction first
            next_i = i + r[direction]
            next_j = j + c[direction]

            if 0 <= next_i < n and 0 <= next_j < n and mat[next_i][next_j] == 0:
                dfs(cnt, mat, next_i, next_j, n, direction)
            else:
                # Change direction if needed
                direction = (direction + 1) % 4
                next_i = i + r[direction]
                next_j = j + c[direction]
                if 0 <= next_i < n and 0 <= next_j < n and mat[next_i][next_j] == 0:
                    dfs(cnt, mat, next_i, next_j, n, direction)

        mat = [[0 for _ in range(n)] for _ in range(n)]
        cnt = [1]  # Counter as a list to pass by reference
        dfs(cnt, mat, 0, 0, n, 0)  # Start DFS from (0, 0) with direction 0 (right)
        return mat