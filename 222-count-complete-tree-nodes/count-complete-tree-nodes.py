# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node: return 0
            left = right = 0
            if node.left:
                left =  1 + solve(node.left)
            if node.right:
                right = 1 + solve(node.right)
            return left + right

        return 1 + solve(root) if root else 0