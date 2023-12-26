class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            root = node
            return root
        if not root.left and val < root.val:
            root.left = node
        elif not root.right and val > root.val:
            root.right = node
        
        elif val < root.val:
            self.insertIntoBST(root.left, val)
        else:
            self.insertIntoBST(root.right, val)
        
        return root