class Solution:
    def convertToAdjList(self, isConnected):
        n,m = len(isConnected), len(isConnected[0])
        adjList = [[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if isConnected[i][j]==1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        return adjList

    def dfs(self, adjList, vis, i):
        vis[i] = True
        for j in adjList[i]:
            if not vis[j]:
                self.dfs(adjList,vis,j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = self.convertToAdjList(isConnected)
        cnt = 0
        n = len(isConnected)
        vis = [False]*(n)
        for i in range(n):
            if not vis[i]:
                self.dfs(adjList, vis, i)
                cnt += 1
        return cnt