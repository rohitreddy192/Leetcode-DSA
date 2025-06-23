class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        x_to_y = defaultdict(int)

        for xi, yi in zip(x, y):
            x_to_y[xi] = max(x_to_y[xi], yi)

        top_y_values = sorted(x_to_y.values(), reverse=True)

        if len(top_y_values) < 3:
            return -1

        return top_y_values[0] + top_y_values[1] + top_y_values[2]