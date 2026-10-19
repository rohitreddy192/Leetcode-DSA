
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0]=1

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            # Number of paths ending at this node
            count = prefix_sum[curr_sum - targetSum]

            # Add current prefix sum
            prefix_sum[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack: remove this node's prefix sum
            prefix_sum[curr_sum] -= 1

            return count

        return dfs(root, 0)
