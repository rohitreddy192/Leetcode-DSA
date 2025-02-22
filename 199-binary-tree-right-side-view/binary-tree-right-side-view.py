# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append((root,0))
        nodes = defaultdict(list)
        maxi = 0
        while q:
            n = len(q)
            for i in range(n):
                node, height = q.popleft()
                nodes[height].append(node.val)
                if node.right:
                    q.append((node.right,height+1))
                if node.left:
                    q.append((node.left, height+1))
                maxi = max(maxi,height)
        
        ans = []
        for i in range(maxi+1):
            ans.append(nodes[i][0])

        return ans

