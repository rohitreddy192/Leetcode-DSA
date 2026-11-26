
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: List['TreeNode']) -> 'TreeNode':
        target = set(nodes)

        def dfs(node):
            if not node:
                return None

            if node in target:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left or right

        return dfs(root)
