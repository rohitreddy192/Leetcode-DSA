# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        if not root.left and not root.right: return [root.val]

        dq = deque()
        dq.append(root)
        
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if i==n-1:
                    res.append(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return res