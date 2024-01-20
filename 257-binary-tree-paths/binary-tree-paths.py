# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def solve(root,ds,l):
            if not root.left and not root.right:
                st = l+"->"+str(root.val)
                ds.append(st[2:])
                return 
            if root.left:
                solve(root.left,ds,l+"->"+str(root.val))
            if root.right:
                solve(root.right,ds,l+"->"+str(root.val))
        ds = []
        solve(root,ds,"")
        return ds
        