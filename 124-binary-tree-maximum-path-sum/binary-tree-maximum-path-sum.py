# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1e9
        def solve(root):
            if not root: return 0
            left = max(solve(root.left), 0)
            right = max(solve(root.right), 0)
            tmp = root.val + left+right
            self.ans = max(self.ans, tmp)
            return max(root.val + left, root.val+right)
        solve(root)
        return self.ans