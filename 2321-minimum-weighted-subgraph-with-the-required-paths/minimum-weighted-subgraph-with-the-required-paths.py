import heapq
from typing import List

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(start, adj):
            dist = [float("inf")] * n
            dist[start] = 0
            min_heap = [(0, start)]
            
            while min_heap:
                curr_dist, node = heapq.heappop(min_heap)
                
                if curr_dist > dist[node]:  # Skip outdated entries
                    continue
                
                for neighbor, weight in adj[node]:
                    new_dist = curr_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(min_heap, (new_dist, neighbor))
            
            return dist

        # Build adjacency list for forward graph and reversed graph
        adj = [[] for _ in range(n)]
        rev_adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w))  # Normal graph
            rev_adj[v].append((u, w))  # Reversed graph

        # Run Dijkstra from src1, src2, and dest
        dist1 = dijkstra(src1, adj)
        dist2 = dijkstra(src2, adj)
        dist_dest = dijkstra(dest, rev_adj)

        # Find the best meeting point x
        min_weight = float("inf")
        for x in range(n):
            if dist1[x] < float("inf") and dist2[x] < float("inf") and dist_dest[x] < float("inf"):
                min_weight = min(min_weight, dist1[x] + dist2[x] + dist_dest[x])

        return min_weight if min_weight != float("inf") else -1
