# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        dp = {}
        def solve(root):
            if not root:
                return 0
            
            if root in dp: return dp[root]
            
            pick = root.val 
            not_pick = solve(root.left) + solve(root.right)

            tmp = 0
            if root.left:
                tmp = solve(root.left.left) + solve(root.left.right)
            if root.right:
                tmp += (solve(root.right.left) + solve(root.right.right))

            pick = pick + tmp

            dp[root] =  max(pick, not_pick)
            return dp[root]

        return solve(root)