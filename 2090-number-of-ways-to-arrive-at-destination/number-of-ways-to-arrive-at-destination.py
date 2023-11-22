from heapq import heappop, heappush
from math import inf

class Solution:
    def countPaths(self, n, a):
        adj = [[] for _ in range(n)]
        for it in a:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))

        ways = [0] * n
        dist = [inf] * n
        pq = [(0, 0)]  # (dist, node)
        dist[0] = 0
        ways[0] = 1

        while pq:
            d, node = heappop(pq)
            for adjnode, wt in adj[node]:
                if d + wt < dist[adjnode]:
                    dist[adjnode] = d + wt
                    ways[adjnode] = ways[node]
                    heappush(pq, (dist[adjnode], adjnode))
                elif d + wt == dist[adjnode]:
                    ways[adjnode] = (ways[adjnode] + ways[node]) % 1000000007

        return ways[n - 1] % 1000000007
