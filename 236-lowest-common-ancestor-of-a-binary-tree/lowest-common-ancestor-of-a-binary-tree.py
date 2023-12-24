# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 0
        def solve(node,p,q):
            if not node or node==p or node==q:
                return node
            leftNode = solve(node.left,p,q)
            rightNode = solve(node.right,p,q)
            if not leftNode:
                return rightNode
            elif not rightNode:
                return leftNode
            else:
                return node
        return solve(root,p,q)
        