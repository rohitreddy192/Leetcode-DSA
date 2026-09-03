# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ansdict = defaultdict(list)
        todo = deque([(root, 0, 0)])
        while todo:
            node, level, view = todo.popleft()
            ansdict[level].append(view)
            view = view-1
            if node.left:
                todo.append((node.left,level+1,2*view + 1))
            if node.right:
                todo.append((node.right,level+1, 2*view + 2))
        ans = 0
        for i in sorted(ansdict):
            ans  = max(ans, max(ansdict[i])-min(ansdict[i])+1)
        return ans