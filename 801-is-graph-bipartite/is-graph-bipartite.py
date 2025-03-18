class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(src,color):
            q = deque()
            q.append((src,0))
            color[src] = 0

            while q:
                node, col = q.popleft()
                for n1 in graph[node]:
                    if color[n1] not in (-1, 1-col):
                        return False
                    else:
                        if color[n1] == -1:
                            color[n1] = 1-col
                            q.append((n1, 1-col))
            
            return True
        
        color = [-1]*(len(graph))
        
        for i in range(len(graph)):
            if color[i]==-1:
                if not bfs(i,color):
                    return False
        return True
