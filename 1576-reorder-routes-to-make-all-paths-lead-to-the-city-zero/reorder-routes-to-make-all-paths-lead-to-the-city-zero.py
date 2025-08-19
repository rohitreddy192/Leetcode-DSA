class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dq = deque()
        adjList = [[] for _ in range(n)]
        for i,j in connections:
            adjList[i].append([j,1])
            adjList[j].append([i,0])
        
        dq.append(0)
        ans = 0
        vis = [False for _ in range(n)]
        vis[0] = True
        while dq:
            node = dq.popleft()
            for i,j in adjList[node]:
                if not vis[i]:
                    vis[i] = True
                    ans += j
                    dq.append(i)
        return ans
                