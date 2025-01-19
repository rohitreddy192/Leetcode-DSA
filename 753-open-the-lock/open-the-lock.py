class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def childrens(state):
            res = []
            for i in range(4):
                digit = str((int(state[i]) + 1)%10)
                res.append(state[:i]+digit+state[i+1:])
                digit = str((int(state[i]) - 1 + 10)%10)
                res.append(state[:i]+digit+state[i+1:])
            return res

        vis = set(deadends)
        q = deque()
        q.append(["0000",0])
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            for child in childrens(state):
                if child not in vis:
                    vis.add(child)
                    q.append([child,turns+1])
        
        return -1

