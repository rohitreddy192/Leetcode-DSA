class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()  # Sort events by start time
        n = len(events)
        memo = {}  # Memoization

        def dfs(i, remaining_k):
            if remaining_k == 0 or i == n:  # Base case
                return 0
            if (i, remaining_k) in memo:  # Memoized result
                return memo[(i, remaining_k)]
            
            # Not picking this event
            not_pick = dfs(i + 1, remaining_k)
            
            # Picking this event, find next non-overlapping event
            next_idx = i + 1
            while next_idx < n and events[next_idx][0] <= events[i][1]:  # Linear search
                next_idx += 1

            pick = events[i][2] + dfs(next_idx, remaining_k - 1)  # Pick this event

            # Store the best result
            memo[(i, remaining_k)] = max(pick, not_pick)
            return memo[(i, remaining_k)]

        return dfs(0, k)