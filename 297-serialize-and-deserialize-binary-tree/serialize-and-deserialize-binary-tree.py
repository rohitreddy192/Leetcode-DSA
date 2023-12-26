# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return ""
        q = deque()
        serialized_str = ""
        q.append(root)
        while q:
            node = q.popleft()
            serialized_str = serialized_str + (str(node.val)+"," if node else "#,")
            if node:
                q.append(node.left)
                q.append(node.right)
        return serialized_str
            
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = [root]
        i = 1
        
        while q:
            node = q.pop(0)
            if values[i] != "#":
                left = TreeNode(int(values[i]))
                node.left = left
                q.append(left)
            i += 1
            
            if values[i] != "#":
                right = TreeNode(int(values[i]))
                node.right = right
                q.append(right)
            i += 1
        
        return root
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))