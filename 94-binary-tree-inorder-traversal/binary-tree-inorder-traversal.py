# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        def inorder(root):
            if not root: return
            inorder(root.left) 
            st.append(root.val)
            inorder(root.right)
        inorder(root)
        return st
        
        """inOrder = []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack: break
                else:
                    node = stack.pop()
                    inOrder.append(node.val)
                    node = node.right
        return inOrder"""