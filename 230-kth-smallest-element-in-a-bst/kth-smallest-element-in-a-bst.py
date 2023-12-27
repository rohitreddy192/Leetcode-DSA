# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, arr, cnt):
            if not root: return
            inOrder(root.left,arr,cnt)
            cnt[0] += 1
            if cnt[0] == k:
                arr.append(root.val)
                return 
            inOrder(root.right,arr,cnt)
        arr = []
        cnt = [0]
        inOrder(root,arr,cnt)
        return arr[0]