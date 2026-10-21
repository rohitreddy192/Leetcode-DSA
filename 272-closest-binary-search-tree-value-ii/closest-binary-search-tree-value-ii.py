# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode | None, target: float, k: int) -> list[int]:
        kClosestHeap = []

        def dfs(root):
            if not root:
                return 
            
            heapq.heappush(kClosestHeap, (abs(root.val-target), root.val))
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        
        result = []
        while kClosestHeap and k>0:
            _, val = heapq.heappop(kClosestHeap)
            result.append(val)
            k -= 1
            
        return result