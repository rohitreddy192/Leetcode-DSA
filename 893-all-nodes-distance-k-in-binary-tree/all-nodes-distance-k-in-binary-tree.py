# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}
        temp = root
        todo = deque()
        todo.append(temp)
        while todo:
            node = todo.popleft()
            if node.left:
                parentMap[node.left] = node
                todo.append(node.left)
            if node.right:
                parentMap[node.right] = node
                todo.append(node.right)
        vis = {}
        vis[target] = True
        ans = []
        currLevel = 0
        todo.append(target)
        while todo:
            if currLevel == k: break
            currLevel += 1
            size = len(todo)
            for i in range(size):
                node = todo.popleft()
                if node.left and node.left not in vis:
                    todo.append(node.left)
                    vis[node.left] = True
                if node.right and node.right not in vis:
                    todo.append(node.right)
                    vis[node.right] = True
                if parentMap.get(node) and parentMap.get(node) not in vis:
                    todo.append(parentMap.get(node))
                    vis[parentMap.get(node)] = True
        while todo:
            node = todo.popleft()
            ans.append(node.val)
        return ans



