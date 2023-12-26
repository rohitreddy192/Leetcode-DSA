# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(postStart,postEnd, inStart, inEnd, mpp):
            if postStart>postEnd or inStart>inEnd: return None

            root = TreeNode(postorder[postEnd])
            inRoot = mpp[root.val]
            n_elem = inEnd - inRoot

            root.right = construct(postEnd-n_elem,postEnd-1,inRoot+1, inEnd,mpp)
            root.left = construct(postStart,postEnd-n_elem-1, inStart, inRoot-1, mpp)

            return root
        
        postStart, postEnd = 0, len(postorder)-1
        inStart, inEnd = 0, len(inorder)-1
        mpp = {val:idx for idx,val in enumerate(inorder)}
        return construct(postStart,postEnd,inStart,inEnd,mpp)