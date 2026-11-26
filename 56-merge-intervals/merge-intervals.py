import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        heap = []

        for start, end in intervals:
            heapq.heappush(heap, (start, end))

        res = []

        start, end = heapq.heappop(heap)

        while heap:
            curr_start, curr_end = heapq.heappop(heap)

            if curr_start <= end:
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end

        res.append([start, end])

        return res