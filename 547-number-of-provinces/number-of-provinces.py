class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    adj[i].append(j)
        
        vis = [False for _ in range(n)]
        def dfs(node):
            vis[node] = True
            for nxt_node in adj[node]:
                if not vis[nxt_node]:
                    dfs(nxt_node)
        cnt = 0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                cnt += 1
        
        return cnt