class Unionfind:
    def __init__(self, n):
        self.weight = [1e9]*(n)
        self.parent = [i for i in range(n)]
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u,v):
        rootU, rootV = self.find(u), self.find(v)
        if rootU == rootV:
            return 
        
        if self.weight[rootU] < self.weight[rootV]:
            rootU, rootV = rootV, rootU

        self.weight[rootV] += self.weight[rootU]
        self.parent[rootU] = self.parent[rootV]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        uf = Unionfind(n)
        for u,v,w in edges:
            uf.union(u,v)

        component_cost = {}
        for u,v,w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w
        
        res = []
        for src, dest in query:
            r1, r2 = uf.find(src), uf.find(dest)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])
        
        return res
        