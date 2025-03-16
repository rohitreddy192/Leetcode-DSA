class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        vis = [False]*(n)
        def dfs(i):
            vis[i] = True
            for node in adj[i]:
                if not vis[node]:
                    dfs(node)
        
        cnt = 0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                cnt += 1
        
        return cnt