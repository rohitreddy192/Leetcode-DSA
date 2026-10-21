# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        
        self.ans = 0
        def dfs(root):
            if not root:
                return 1

            left = dfs(root.left)
            right = dfs(root.right)

            if left == 0 or right == 0: # Children are not covered by camera
                self.ans += 1
                return 2

            if left == 2 or right == 2:
                return 1

            return 0
        
        if dfs(root) == 0:
            self.ans += 1
        return self.ans