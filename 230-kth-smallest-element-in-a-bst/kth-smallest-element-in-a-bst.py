# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, arr):
            if not root: return
            inOrder(root.left,arr)
            arr.append(root.val)
            inOrder(root.right,arr)
        arr = []
        inOrder(root,arr)
        n = len(arr)
        if k > n: return -1
        return arr[k-1]