import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class MaxStack:

    def __init__(self):
        self.head = Node(0)     # dummy head
        self.tail = Node(0)     # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.heap = []          # max-heap (-val, id, node)
        self.uid = 0            # unique id counter
        self.valid = {}         # map from uid → node (still in stack)

    def _addNode(self, node):
        # insert before tail
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def _removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def push(self, x: int) -> None:
        node = Node(x)
        self._addNode(node)
        self.uid += 1
        heapq.heappush(self.heap, (-x, -self.uid, node))
        self.valid[node] = True

    def pop(self) -> int:
        node = self.tail.prev
        self._removeNode(node)
        self.valid[node] = False
        return node.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        # remove invalid heap entries
        while self.heap and not self.valid[self.heap[0][2]]:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        # remove invalid heap entries
        while self.heap and not self.valid[self.heap[0][2]]:
            heapq.heappop(self.heap)
        _, _, node = heapq.heappop(self.heap)
        self._removeNode(node)
        self.valid[node] = False
        return node.val
