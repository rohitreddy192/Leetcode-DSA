class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # u -> v
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*(numCourses)
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        res = []
        dq = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                dq.append(i)
                res.append(i)

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                for nn in adj[node]:
                    if indegree[nn]>0:
                        indegree[nn] -= 1
                        if indegree[nn] == 0:
                            dq.append(nn)
                            res.append(nn)
        
        return len(res)==numCourses