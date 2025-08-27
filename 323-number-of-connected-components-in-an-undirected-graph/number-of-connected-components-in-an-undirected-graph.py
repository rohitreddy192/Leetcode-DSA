class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = set()
        def dfs(node,vis):
            if node not in vis:
                vis.add(node)
                for neigh in adj[node]:
                    if neigh not in vis:
                        dfs(neigh, vis)
        
        cnt = 0
        for i in range(n):
            if i not in vis:
                cnt += 1
                dfs(i, vis)
        
        return cnt