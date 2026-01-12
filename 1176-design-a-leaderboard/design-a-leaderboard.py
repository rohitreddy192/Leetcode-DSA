class Node:
    def __init__(self, score=0):
        self.score = score
        self.prev = None
        self.next = None


class Leaderboard:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.player_node_map = {}
        self.player_score_map = {}

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _clearPlayerIdAndScore(self, playerId):
        if playerId in self.player_node_map:
            self._remove(self.player_node_map[playerId])
            del self.player_node_map[playerId]

    def addScore(self, playerId: int, score: int) -> None:
        old_score = self.player_score_map.get(playerId, 0)
        new_score = old_score + score
        self.player_score_map[playerId] = new_score

        self._clearPlayerIdAndScore(playerId)

        curr = self.tail.prev
        while curr != self.head and new_score < curr.score:
            curr = curr.prev

        new_node = Node(new_score)
        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node

        self.player_node_map[playerId] = new_node

    def top(self, K: int) -> int:
        curr = self.tail.prev
        total = 0

        while curr != self.head and K > 0:
            total += curr.score
            curr = curr.prev
            K -= 1

        return total

    def reset(self, playerId: int) -> None:
        if playerId in self.player_score_map:
            del self.player_score_map[playerId]
        self._clearPlayerIdAndScore(playerId)
