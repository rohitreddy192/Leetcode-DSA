# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root,0,0))
        nodes = defaultdict(lambda : defaultdict(list))
        mini, maxi = 0, 0
        while q:
            node, x, y = q.popleft()
            nodes[x][y].append(node.val)
            if node.left:
                q.append((node.left,x-1,y+1))
            if node.right:
                q.append((node.right,x+1,y+1))
            mini = min(mini, x)
            maxi = max(maxi,x)
        
        res = []
        for i in range(mini,maxi+1):
            tmp = nodes[i]
            ans = []
            for x, y in nodes[i].items():
                ans.extend(sorted(y[:]))
            if ans:
                res.append(ans[:])
        
        return res


