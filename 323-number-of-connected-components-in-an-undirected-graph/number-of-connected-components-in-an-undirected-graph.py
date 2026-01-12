class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, vis, adj):
            vis[node] = True
            for ne in adj[node]:
                if not vis[ne]:
                    dfs(ne, vis, adj)
            

        cnt = 0
        vis = [False for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            if not vis[i]:
                dfs(i, vis, adj)
                cnt += 1
        
        return cnt