class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            idx, op, time = log.split(":")
            idx, time = int(idx), int(time)

            if op == "start":
                if stack:
                    res[stack[-1]] += time - prev_time

                stack.append(idx)
                prev_time = time

            else:  # end
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res