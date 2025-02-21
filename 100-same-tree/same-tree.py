# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(not p and not q): return True
        if(p and q) and (p.val!=q.val): return False
        if(p and not q) or (not p and q): return False
        return Solution().isSameTree(p.left,q.left) and Solution().isSameTree(p.right,q.right)
