from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0  # Already at the destination
        
        # Step 1: Build the Graph
        stop_to_buses = defaultdict(set)  # stop -> buses that pass through it
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(bus_id)

        # Step 2: BFS Initialization
        queue = deque()  # (bus_count, current_stop)
        visited_stops = set()  # Stops we have visited
        visited_buses = set()  # Buses we have taken

        # Add all buses we can take from the source stop
        for bus_id in stop_to_buses[source]:
            for stop in routes[bus_id]:
                queue.append((1, stop))  # Taking first bus
                visited_stops.add(stop)
            visited_buses.add(bus_id)

        # Step 3: BFS Traversal
        while queue:
            bus_count, stop = queue.popleft()

            if stop == target:
                return bus_count  # Found the shortest path
            
            # Check all buses passing through this stop
            for bus_id in stop_to_buses[stop]:
                if bus_id in visited_buses:
                    continue  # Don't take the same bus twice
                
                # Explore all stops in this bus route
                for next_stop in routes[bus_id]:
                    if next_stop not in visited_stops:
                        queue.append((bus_count + 1, next_stop))
                        visited_stops.add(next_stop)
                
                visited_buses.add(bus_id)  # Mark bus as used
        
        return -1  # Target not reachable
