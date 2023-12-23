# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inOrder = []
        if not root: return inOrder
        st = []
        curr = root
        while 1:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                if not st: break
                curr = st.pop()
                inOrder.append(curr.val)
                curr = curr.right
        return inOrder