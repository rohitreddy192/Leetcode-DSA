# from typing import List, Optional

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []  # Fix: Handle empty tree case
        
        self.left = []
        self.right = []
        self.leaves = []

        def isLeaf(node):
            return node and not node.left and not node.right

        def getLeft(node):
            if node and not isLeaf(node):
                self.left.append(node.val)  # Add only non-leaf nodes
            if node and node.left:
                getLeft(node.left)
            elif node and node.right:
                getLeft(node.right)  # Only if left is missing

        def getRight(node):
            if node and not isLeaf(node):
                self.right.append(node.val)  # Add only non-leaf nodes
            if node and node.right:
                getRight(node.right)
            elif node and node.left:
                getRight(node.left)  # Only if right is missing

        def getLeaves(node):
            if not node:
                return
            if isLeaf(node):
                self.leaves.append(node.val)
            getLeaves(node.left)
            getLeaves(node.right)

        # Collect boundary nodes
        if not isLeaf(root):  # Root should only be included if it's not a leaf
            result = [root.val]
        else:
            result = []

        getLeft(root.left)
        getLeaves(root)
        getRight(root.right)

        return result + self.left + self.leaves + self.right[::-1]  # Reverse right boundary
