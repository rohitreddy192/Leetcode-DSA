
class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        res = []
        added = False

        for start, end in self.intervals:
            if end < left:
                # Existing interval is completely before new range
                res.append([start, end])

            elif right < start:
                # Existing interval is completely after new range
                if not added:
                    res.append([left, right])
                    added = True
                res.append([start, end])

            else:
                # Overlapping or adjacent intervals: merge
                left = min(left, start)
                right = max(right, end)

        if not added:
            res.append([left, right])

        self.intervals = res

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.intervals:
            if start <= left and right <= end:
                return True

            if start > left:
                return False

        return False

    def removeRange(self, left: int, right: int) -> None:
        res = []

        for start, end in self.intervals:
            # No overlap
            if end <= left or start >= right:
                res.append([start, end])
            else:
                # Preserve the left portion
                if start < left:
                    res.append([start, left])

                # Preserve the right portion
                if end > right:
                    res.append([right, end])

        self.intervals = res
