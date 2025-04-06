class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque()
        q.append(start)

        vis = set()
        vis.add(start)
        while q:
            node = q.popleft()
            if arr[node]==0:
                return True
            vals = [node + arr[node], node - arr[node]]
            for val in vals:
                if 0<=val<n and val not in vis:
                    vis.add(val)
                    q.append(val)
        
        return False