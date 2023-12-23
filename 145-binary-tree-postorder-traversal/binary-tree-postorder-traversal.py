# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postOrder = []
        if not root: return postOrder
        st = []
        curr = root
        while curr or st:
            if curr:
                postOrder.append(curr.val)
                st.append(curr)
                curr = curr.right
            else:
                curr = st.pop().left
        return postOrder[::-1]
        