class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort intervals by start time
        intervals.sort()

        # Step 2: Min-Heap to store end times
        min_heap = []

        for start, end in intervals:
            # If a room is free, remove it from heap
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)  # Free up the room
            
            # Allocate new room (Add current meeting's end time)
            heapq.heappush(min_heap, end)

        # The size of heap is the number of rooms required
        return len(min_heap)