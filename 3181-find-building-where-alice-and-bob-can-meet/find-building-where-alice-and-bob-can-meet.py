class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.tree[node] = l
        else:
            mid = (l + r) // 2
            self.build(2 * node + 1, l, mid)
            self.build(2 * node + 2, mid + 1, r)
            left = self.tree[2 * node + 1]
            right = self.tree[2 * node + 2]
            self.tree[node] = left if self.data[left] >= self.data[right] else right

    # Query for first index > threshold in range [ql, qr]
    def query(self, threshold, ql):
        return self._query(0, 0, self.n - 1, ql, self.n - 1, threshold)

    def _query(self, node, l, r, ql, qr, threshold):
        if r < ql or l > qr:
            return -1
        if l >= ql and r <= qr:
            if self.data[self.tree[node]] <= threshold:
                return -1
        if l == r:
            return l if self.data[l] > threshold else -1

        mid = (l + r) // 2
        left_res = self._query(2 * node + 1, l, mid, ql, qr, threshold)
        if left_res != -1:
            return left_res
        return self._query(2 * node + 2, mid + 1, r, ql, qr, threshold)

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        st = SegmentTree(heights)
        res = []
        for a, b in queries:
            if a == b:
                res.append(a)
                continue
            if a > b:
                a, b = b, a
            ha, hb = heights[a], heights[b]
            if ha < hb:
                res.append(b)
                continue
            max_h = max(ha, hb)
            idx = st.query(max_h, b + 1)
            res.append(idx)
        return res
