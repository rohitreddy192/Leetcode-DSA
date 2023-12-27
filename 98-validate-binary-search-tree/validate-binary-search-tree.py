# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right): return True
        def solve(root, minVal, maxVal):
            if not root: return True
            if root.val <= minVal or root.val >= maxVal: return False
            return solve(root.right, root.val,maxVal) and solve(root.left,minVal, root.val)
        return solve(root,float("-inf"), float("inf"))