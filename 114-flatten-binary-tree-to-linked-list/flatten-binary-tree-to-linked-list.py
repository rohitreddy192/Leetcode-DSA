# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None
        def solve(root):
            nonlocal prev
            if not root: return
            solve(root.right)
            solve(root.left)
            root.right = prev
            root.left = None
            prev = root
        solve(root)
        return prev
        
        """
        Do not return anything, modify root in-place instead.
        """
        