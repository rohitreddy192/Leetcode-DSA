class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dfs(depth, index):
            if index >= len(traversal):
                return None, index

            # Count dashes to determine depth
            dashes = 0
            while index < len(traversal) and traversal[index] == "-":
                dashes += 1
                index += 1
            
            # If depth doesn't match, return back
            if dashes != depth:
                return None, index - dashes

            # Extract the number (node value)
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            
            node = TreeNode(value)

            # Recursively process left and right children
            node.left, index = dfs(depth + 1, index)
            node.right, index = dfs(depth + 1, index)

            return node, index

        root, _ = dfs(0, 0)
        return root
