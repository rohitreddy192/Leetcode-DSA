# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def solve(root):
            if not root: return [0,0]

            l = solve(root.left)
            r = solve(root.right)
            self.ans += (abs(l[0]+r[0]+1 - (l[1]+r[1]+root.val)))

            return [l[0]+r[0]+1, root.val+l[1]+r[1]]
        solve(root)
        return self.ans