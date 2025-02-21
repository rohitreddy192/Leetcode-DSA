# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def depth(node):
            if not node: return 0
            lh = depth(node.left)
            rh = depth(node.right)
            self.maxi = max(self.maxi,lh+rh)
            return 1 + max(lh,rh)
        self.maxi
        depth(root)
        return self.maxi