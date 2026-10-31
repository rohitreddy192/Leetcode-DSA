class TreeAncestor:

    def __init__(self, n, parent):
        self.parent = parent
        self.B = int(n ** 0.5) + 1

        self.jump = [-1] * n

        for node in range(n):
            curr = node

            for _ in range(self.B):
                if curr == -1:
                    break
                curr = parent[curr]

            self.jump[node] = curr

    def getKthAncestor(self, node, k):
        while k >= self.B and node != -1:
            node = self.jump[node]
            k -= self.B

        while k > 0 and node != -1:
            node = self.parent[node]
            k -= 1

        return node