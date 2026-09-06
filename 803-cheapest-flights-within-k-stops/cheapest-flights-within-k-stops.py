class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w in flights:
            adj[u].append((v, w))

        hp = []
        heapq.heappush(hp, (0, src, k + 1))

        dist = defaultdict(lambda: float("inf"))
        dist[(src, k + 1)] = 0

        while hp:
            cost, node, rem_k = heapq.heappop(hp)

            if node == dst:
                return cost

            if rem_k == 0:
                continue

            for nei, price in adj[node]:
                new_cost = cost + price
                new_rem_k = rem_k - 1

                if new_cost < dist[(nei, new_rem_k)]:
                    dist[(nei, new_rem_k)] = new_cost
                    heapq.heappush(
                        hp,
                        (new_cost, nei, new_rem_k)
                    )

        return -1