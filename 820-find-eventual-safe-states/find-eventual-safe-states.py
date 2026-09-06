class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0]*(n)

        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                indegree[i] += 1
        
        dq = deque()

        for i in range(n):
            if indegree[i] == 0:
                dq.append(i)
        
        ans = []
        while dq:
            node = dq.popleft()
            ans.append(node)
            for nn in adj[node]:
                indegree[nn] -= 1
                if indegree[nn]==0:
                    dq.append(nn)
        
        return sorted(ans)