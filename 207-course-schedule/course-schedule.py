class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*(numCourses)
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return len(ans)==numCourses