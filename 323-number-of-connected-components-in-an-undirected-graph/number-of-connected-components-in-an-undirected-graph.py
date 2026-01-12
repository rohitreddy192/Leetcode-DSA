from typing import List
from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * n
        cnt = 0

        for i in range(n):
            if not vis[i]:
                cnt += 1
                dq = deque([i])
                vis[i] = True

                while dq:
                    node = dq.popleft()
                    for ne in adj[node]:
                        if not vis[ne]:
                            vis[ne] = True
                            dq.append(ne)

        return cnt
