import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = [(i.start, i.end) for emp in schedule for i in emp]
        heapq.heapify(heap)

        free = []
        _, end = heapq.heappop(heap)

        while heap:
            start, finish = heapq.heappop(heap)

            if start > end:
                free.append(Interval(end, start))
                end = finish
            else:
                end = max(end, finish)

        return free