
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        occupied = []
        count = [0] * n

        for start, end in meetings:

            # Release all rooms whose meetings have finished
            while occupied and occupied[0][0] <= start:
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))

            else:
                # Delay the meeting until the earliest room is free
                end_time, room = heapq.heappop(occupied)

                duration = end - start
                new_end = end_time + duration

                heapq.heappush(occupied, (new_end, room))

            count[room] += 1

        return count.index(max(count))
