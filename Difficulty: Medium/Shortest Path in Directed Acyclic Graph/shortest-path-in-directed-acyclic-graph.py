from collections import deque
class Solution:
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
        
        dist = [1e9 for _ in range(V)]
        
        start = 0
        dq = deque()
        dist[start] = 0
        dq.append((start, 0))
        
        while dq:
            node, weight = dq.popleft()
            
            for nx_node, nx_weight in adj[node]:
                if dist[nx_node] > nx_weight+weight:
                    dist[nx_node] = nx_weight+weight
                    dq.append((nx_node, dist[nx_node]))
        
        for i in range(V):
            if dist[i] == 1e9:
                dist[i] = -1
        return dist