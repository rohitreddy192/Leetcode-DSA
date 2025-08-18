from collections import defaultdict

class Solution:
    def minEdgeReversals(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)

        # Build graph with weighted edges
        for u, v in edges:
            graph[u].append((v, 0))  # u -> v is correct, no reversal
            graph[v].append((u, 1))  # v -> u would need reversal

        ans = [0] * n

        # Step 1: initial DFS to calculate reversals for root=0
        def dfs1(u, parent):
            res = 0
            for v, cost in graph[u]:
                if v == parent: 
                    continue
                res += cost + dfs1(v, u)
            return res

        ans[0] = dfs1(0, -1)

        # Step 2: re-rooting DFS
        def dfs2(u, parent):
            for v, cost in graph[u]:
                if v == parent: 
                    continue
                if cost == 0:
                    # edge u->v, reversing needed when rooted at v
                    ans[v] = ans[u] + 1
                else:
                    # edge v->u, no longer needs reversal when rooted at v
                    ans[v] = ans[u] - 1
                dfs2(v, u)

        dfs2(0, -1)

        return ans
