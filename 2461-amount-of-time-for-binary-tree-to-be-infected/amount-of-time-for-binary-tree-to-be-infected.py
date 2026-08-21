# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        curr = root
        dq = deque()
        dq.append(curr)
        while dq:
            curr = dq.popleft()
            if curr.left:
                dq.append(curr.left)
                adj[curr.left.val].append(curr.val)
                adj[curr.val].append(curr.left.val)
            
            if curr.right:
                dq.append(curr.right)
                adj[curr.right.val].append(curr.val)
                adj[curr.val].append(curr.right.val)

        dq.clear()
        dq.append((start,0))
        vis = set()
        vis.add(start)
        max_time = 0
        while dq:
            for _ in range(len(dq)):
                node, t = dq.popleft()
                for nxt_node in adj[node]:
                    if nxt_node not in vis:
                        dq.append((nxt_node, t+1))
                        vis.add(nxt_node)
                max_time = max(max_time, t)
        
        if len(vis) == len(adj): return max_time
        return -1