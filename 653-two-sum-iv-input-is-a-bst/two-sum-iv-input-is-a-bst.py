# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mpp = {}
        def solve(root):
            if not root: return False
            if k-root.val in mpp:
                return True
            mpp[root.val] = True
            
            if solve(root.left) or solve(root.right):
                return True
            
            return False
        
        return solve(root)
