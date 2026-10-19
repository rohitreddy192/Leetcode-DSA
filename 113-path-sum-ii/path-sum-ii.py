
from collections import deque

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []

        dq = deque([(root, root.val, [root.val])])
        ans = []

        while dq:
            node, curr_sum, path = dq.popleft()

            if curr_sum == targetSum and not node.left and not node.right:
                ans.append(path)

            if node.left:
                dq.append((
                    node.left,
                    curr_sum + node.left.val,
                    path + [node.left.val]
                ))

            if node.right:
                dq.append((
                    node.right,
                    curr_sum + node.right.val,
                    path + [node.right.val]
                ))

        return ans
