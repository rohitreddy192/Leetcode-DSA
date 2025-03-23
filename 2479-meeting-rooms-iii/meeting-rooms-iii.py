class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Step 1: Sort meetings by start time
        meetings.sort()

        # Min-Heap to track (end_time, room)
        occupied_rooms = []
        
        # Min-Heap to track available rooms (smallest index first)
        available_rooms = list(range(n))  # Initially all rooms are available
        heapq.heapify(available_rooms)
        
        # Track meeting counts for each room
        meeting_counts = [0] * n

        # Step 2: Process each meeting
        for start, end in meetings:
            # Free up rooms that have finished before the current meeting starts
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)  # Room is now available

            # Step 3: Assign the meeting to the lowest available room
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room))
            else:
                # Delay the meeting to the earliest available room
                end_time, room = heapq.heappop(occupied_rooms)
                new_end = end_time + (end - start)  # Maintain duration
                heapq.heappush(occupied_rooms, (new_end, room))

            # Step 4: Update the meeting count
            meeting_counts[room] += 1

        # Step 5: Find the room with the most meetings
        max_meetings = max(meeting_counts)
        return meeting_counts.index(max_meetings)
