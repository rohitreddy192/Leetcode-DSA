# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return 0, True
            
            left = depth(root.left)
            right = depth(root.right)
            if not(left[1] and right[1]) or abs(right[0]-left[0])>1:
                return 10**9, False

            return (1+max(left[0], right[0]), (left[1] or right[1]))
        _, ans = depth(root)

        return ans