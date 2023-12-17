# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root,maxVal):
            if not root:return 0
            left = max(0,solve(root.left,maxVal))
            right = max(0,solve(root.right,maxVal))
            maxVal[0] = max(maxVal[0],left+right+root.val)
            return root.val+max(left,right)

        maxVal = [-10**9]
        solve(root,maxVal)
        return maxVal[0]