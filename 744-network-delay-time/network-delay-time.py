class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hp= []
        adj = [[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append((v,t))
        heapq.heappush(hp, (0,k))
        max_t = defaultdict(lambda: float("inf"))
        max_t[k] = 0
        while hp:
            time, node = heapq.heappop(hp)
            for nn, t in adj[node]:
                if max_t[nn] > time + t:
                    heapq.heappush(hp, (time+t, nn))
                    max_t[nn] = time+t
        
        return max(max_t.values()) if len(max_t.values())==n else -1