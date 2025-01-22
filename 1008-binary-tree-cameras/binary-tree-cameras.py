# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 1  # Null nodes are considered covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:  # If any child is not covered
                self.ans += 1
                return 2  # Place a camera here
            
            if left == 2 or right == 2:  # If any child has a camera
                return 1  # This node is covered
            
            return 0  # This node is not covered
        
        # If the root itself is not covered, add a camera
        if dfs(root) == 0:
            self.ans += 1
        
        return self.ans