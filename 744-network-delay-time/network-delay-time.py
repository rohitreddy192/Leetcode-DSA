class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hp = []
        adj = [[] for _ in range(n+1)]

        for u, v, t in times:
            adj[u].append((v, t))

        heapq.heappush(hp, (0, k))

        dist = defaultdict(lambda: float("inf"))
        dist[k] = 0

        while hp:
            time, node = heapq.heappop(hp)

            if time > dist[node]:
                continue

            for nei, t in adj[node]:
                new_time = time + t

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(hp, (new_time, nei))

        return max(dist.values()) if len(dist) == n else -1