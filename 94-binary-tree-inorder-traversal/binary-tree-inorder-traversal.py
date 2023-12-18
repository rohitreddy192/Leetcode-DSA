# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root,inO):
            if not root: return
            solve(root.left,inO)
            inO.append(root.val)
            solve(root.right,inO)
        inO = []
        solve(root,inO)
        return inO