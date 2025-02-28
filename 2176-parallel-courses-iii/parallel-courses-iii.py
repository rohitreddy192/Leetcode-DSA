class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree = [0]*(n+1)
        for u,v in relations:
            adj[u].append(v)
            indegree[v] += 1

        max_time = [0]*(n+1)
        q = deque()
        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)        
                max_time[i] = time[i-1]

        ans = 0
        while q:
            ni = len(q)
            for i in range(ni):
                node = q.popleft()
                # maxi = max(maxi, time[node-1])
                for n in adj[node]:
                    indegree[n] -= 1
                    max_time[n] = max(max_time[n], max_time[node]+time[n-1])
                    if indegree[n]==0:
                        q.append(n)
        return max(max_time)