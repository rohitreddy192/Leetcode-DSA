class Solution:
    def alienOrder(self, alien_dict: List[str]) -> str:
        adj = defaultdict(list)
        N = len(alien_dict)
        indegree = defaultdict(int)
        for word in alien_dict:
            for char in word:
                indegree[char] = 0
        for i in range(N-1):
            word1 = alien_dict[i]
            word2 = alien_dict[i+1]
            len1, len2 = len(word1), len(word2)
            if len1>len2 and word1[:len2]==word2[:]:
                return ""
            for j in range(min(len1,len2)):
                if alien_dict[i][j] != alien_dict[i+1][j]:
                    adj[alien_dict[i][j]].append(alien_dict[i+1][j])
                    indegree[alien_dict[i+1][j]] += 1
                    break

        print(indegree)
        q = deque()
        for u,v in indegree.items():
            if v==0:
                q.append(u)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return "".join(ans) if len(ans)==len(indegree) else ""