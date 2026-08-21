class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.solve(numCourses, prerequisites)
    def solve(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        adj = [[] for _ in range(numCourses)]
        vis = set()
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        dq = deque()
        ans = []
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
                ans.append(i)
                vis.add(i)
        
        while dq:
            
            node = dq.popleft()
            for nxt_node in adj[node]:
                indegree[nxt_node] -= 1
                if indegree[nxt_node]==0:
                    dq.append(nxt_node)
                    ans.append(nxt_node)
        
        return ans[::-1] if len(ans)==numCourses else []