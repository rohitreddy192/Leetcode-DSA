# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = -10000
        def depth(root):
            if not root: return 0
            left = max(depth(root.left), 0)
            right = max(depth(root.right), 0)
            self.sum = max(self.sum, root.val+left+right)
            return max(root.val + left,root.val + right)
        
        depth(root)
        return self.sum