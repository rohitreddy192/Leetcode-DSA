class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def add_node(self, new_node):
        temp = self.head.next
        new_node.next = temp
        new_node.prev = self.head
        self.head.next = new_node
        temp.prev = new_node

    def delete_node(self, del_node):
        delprev = del_node.prev
        delnext = del_node.next
        delprev.next = delnext
        delnext.prev = delprev

    def get(self, key_: int) -> int:
        if key_ in self.m:
            res_node = self.m[key_]
            res = res_node.val
            del self.m[key_]
            self.delete_node(res_node)
            self.add_node(res_node)
            self.m[key_] = self.head.next
            return res
        return -1

    def put(self, key_: int, value: int) -> None:
        if key_ in self.m:
            existing_node = self.m[key_]
            del self.m[key_]
            self.delete_node(existing_node)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.delete_node(self.tail.prev)
        self.add_node(self.Node(key_, value))
        self.m[key_] = self.head.next
