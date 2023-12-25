# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct_tree(preorder, pre_start, pre_end, inorder, in_start, in_end, mp):
            if pre_start > pre_end or in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])
            elem = mp[root.val]
            n_elem = elem - in_start

            root.left = construct_tree(preorder, pre_start + 1, pre_start + n_elem, inorder, in_start, elem - 1, mp)
            root.right = construct_tree(preorder, pre_start + n_elem + 1, pre_end, inorder, elem + 1, in_end, mp)

            return root

        pre_start, pre_end = 0, len(preorder) - 1
        in_start, in_end = 0, len(inorder) - 1

        mp = {val: idx for idx, val in enumerate(inorder)}

        return construct_tree(preorder, pre_start, pre_end, inorder, in_start, in_end, mp)