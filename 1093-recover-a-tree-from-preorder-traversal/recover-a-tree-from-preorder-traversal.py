class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i, n = 0, len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1  # Move past dashes to find the number

            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1  # Move past digits to find next node

            node = TreeNode(value)

            # If depth is equal to stack size, it means this is a left child
            while len(stack) > depth:
                stack.pop()

            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]  # Root is at the bottom of the stack
