import heapq

class Solution:
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda x: x[1])

        heap = []  # (end, passengers)
        current = 0

        for passengers, start, end in trips:

            # Drop off passengers who have reached their destination
            while heap and heap[0][0] <= start:
                drop_end, drop_passengers = heapq.heappop(heap)
                current -= drop_passengers

            # Pick up new passengers
            current += passengers

            if current > capacity:
                return False

            heapq.heappush(heap, (end, passengers))

        return True