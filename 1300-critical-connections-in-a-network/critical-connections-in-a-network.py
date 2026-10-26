class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        self.timer = 1

        def dfs(node, parent, adj, vis, tin, low, bridges):
            vis.add(node)
            low[node] = tin[node] = self.timer
            self.timer += 1

            for nnei in adj[node]:
                if nnei == parent: continue
                if nnei not in vis:
                    dfs(nnei, node, adj, vis, tin, low, bridges)

                    low[node] = min(low[node], low[nnei])

                    if low[nnei]>tin[node]:
                        bridges.append([nnei, node])
                
                else:
                    low[node] = min(low[node], low[nnei])
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        tin = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        bridges = []
        vis = set()

        dfs(0,-1,adj, vis, tin, low, bridges)
        return bridges
