class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort by (actual - minimum), ascending
        tasks.sort(key=lambda x: x[0] - x[1])

        initialEnergy = 0
        consumed = 0

        for actual, minimum in tasks:
            initialEnergy = max(
                initialEnergy,
                consumed + minimum
            )

            consumed += actual

        return initialEnergy