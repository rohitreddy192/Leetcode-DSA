# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        def goTillEnd(root):
            if not root.right: return root
            return goTillEnd(root.right)
        def helper(root):
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                rightChild = root.right
                lastRight = goTillEnd(root.left)
                lastRight.right = rightChild
                return root.left
        if not root: return root
        if root.val == k: return helper(root)
        dummy = root
        while root:
            if root.val>k:
                if root.left and root.left.val == k:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == k:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right
        return dummy             
        
        """
        Three Steps:-
            1. Find the key k.
            2. Send the node to delete and replace.
            3. Attach the rest of the part at the end.
        """
