class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def odd_even_jumps(arr):
            n = len(arr)
            # Precompute the next index for odd jumps:
            next_odd = [None] * n
            # We sort indices by (arr[i], i) so that for a given arr[i] we can jump to the smallest valid index j.
            indices = sorted(range(n), key=lambda i: (arr[i], i))
            stack = []
            for i in indices:
                while stack and i > stack[-1]:
                    idx = stack.pop()
                    next_odd[idx] = i
                stack.append(i)

            # Precompute the next index for even jumps:
            next_even = [None] * n
            # We sort indices by (-arr[i], i) so that for a given arr[i] we can jump to the smallest index j
            # with the largest possible value not exceeding arr[i].
            indices = sorted(range(n), key=lambda i: (-arr[i], i))
            stack = []
            for i in indices:
                while stack and i > stack[-1]:
                    idx = stack.pop()
                    next_even[idx] = i
                stack.append(i)

            # Recursion with memoization using lru_cache.
            from functools import lru_cache

            @lru_cache(maxsize=None)
            def canReach(i, odd_jump):
                # If we are at the last index, we have reached the end.
                if i == n - 1:
                    return True

                if odd_jump:
                    nxt = next_odd[i]
                    if nxt is not None:
                        return canReach(nxt, not odd_jump)
                    else:
                        return False
                else:
                    nxt = next_even[i]
                    if nxt is not None:
                        return canReach(nxt, not odd_jump)
                    else:
                        return False

            # Count the number of starting indices (starting with an odd jump)
            count = sum(canReach(i, True) for i in range(n))
            return count
        return odd_even_jumps(arr)
