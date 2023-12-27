# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], k: int) -> Optional[TreeNode]:
        if root is None:
            return root
    
        # Recursive calls for ancestors of
        # node to be deleted
        if root.val > k:
            root.left = self.deleteNode(root.left, k)
            return root
        elif root.val < k:
            root.right = self.deleteNode(root.right, k)
            return root
    
        # We reach here when root is the node
        # to be deleted.
    
        # If one of the children is empty
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
    
        # If both children exist
        else:
    
            succParent = root
    
            # Find successor
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
    
            # Delete successor.  Since successor
            # is always left child of its parent
            # we can safely make successor's right
            # right child as left of its parent.
            # If there is no succ, then assign
            # succ.right to succParent.right
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
    
            # Copy Successor Data to root
            root.val = succ.val
    
            # Delete Successor and return root
            del succ
            return root