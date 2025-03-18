import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Min-Heap (Priority Queue) -> (cost, current_city, stops_used)
        pq = [(0, src, 0)]
        
        # Dictionary to track minimum cost to reach a city with a given number of stops
        best = {}

        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            # If we reach the destination, return the cost
            if city == dst:
                return cost
            
            # If we exceed stop limit, continue
            if stops > k:
                continue
            
            # Explore neighbors
            for neighbor, price in graph[city]:
                new_cost = cost + price
                # Only push into the queue if it's a better option (lower cost or fewer stops)
                if (neighbor, stops) not in best or new_cost < best[(neighbor, stops)]:
                    best[(neighbor, stops)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))

        return -1  # If no path found within k stops
