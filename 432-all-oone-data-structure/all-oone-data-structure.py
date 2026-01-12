class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            # insert freq=1
            if self.head.next.freq == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)
            node.keys.add(key)
            self.key_to_node[key] = node
            return

        node = self.key_to_node[key]
        next_freq = node.freq + 1

        if node.next.freq == next_freq:
            next_node = node.next
        else:
            next_node = Node(next_freq)
            self._insert_after(node, next_node)

        next_node.keys.add(key)
        self.key_to_node[key] = next_node

        node.keys.remove(key)
        if not node.keys:
            self._remove(node)

    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
            return

        node = self.key_to_node[key]
        node.keys.remove(key)

        if node.freq == 1:
            del self.key_to_node[key]
        else:
            prev_freq = node.freq - 1
            if node.prev.freq == prev_freq:
                prev_node = node.prev
            else:
                prev_node = Node(prev_freq)
                self._insert_after(node.prev, prev_node)

            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node

        if not node.keys:
            self._remove(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
