class Solution:
    def recoverTree(self, root):
        inorder = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)

        dfs(root)

        first = second = None

        for i in range(1, len(inorder)):
            if inorder[i - 1].val > inorder[i].val:
                if first is None:
                    first = inorder[i - 1]

                second = inorder[i]

        first.val, second.val = second.val, first.val