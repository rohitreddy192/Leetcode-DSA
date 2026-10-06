class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize constraints
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def solve():

            # Find the empty cell with minimum candidates
            best_cell = None
            best_candidates = None

            for r in range(9):
                for c in range(9):

                    if board[r][c] != ".":
                        continue

                    box = (r // 3) * 3 + (c // 3)

                    candidates = (
                        set("123456789")
                        - rows[r]
                        - cols[c]
                        - boxes[box]
                    )

                    if not candidates:
                        return False

                    if best_candidates is None or len(candidates) < len(best_candidates):
                        best_cell = (r, c, box)
                        best_candidates = candidates

                        # Can't do better than one candidate
                        if len(candidates) == 1:
                            break

                if best_candidates is not None and len(best_candidates) == 1:
                    break

            # No empty cells → solved
            if best_cell is None:
                return True

            r, c, box = best_cell

            for num in best_candidates:

                # Choose
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                # Explore
                if solve():
                    return True

                # Undo
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        solve()