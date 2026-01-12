from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]

        # Find rightmost index where values[i][0] <= timestamp
        idx = bisect.bisect_right(values, (timestamp, chr(127))) - 1

        if idx >= 0:
            return values[idx][1]
        return ""
