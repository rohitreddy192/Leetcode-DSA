class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def solve(root, parent):

            if root is None:
                return 0

            left = solve(root.left, root.val)
            right = solve(root.right, root.val)

            # Path passing through current node
            self.ans = max(self.ans, left + right)

            if root.val == parent:
                return max(left, right) + 1

            return 0

        solve(root, -1)

        return self.ans