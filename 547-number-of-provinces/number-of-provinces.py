class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for i in range(len(isConnected))]
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        vis = [False]*len(isConnected)

        def dfs(node, vis):
            vis[node] = True
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    dfs(neighbor,vis)
        
        cnt = 0
        for i in range(len(isConnected)):
            if not vis[i]:
                cnt += 1
                dfs(i,vis)
        return cnt

