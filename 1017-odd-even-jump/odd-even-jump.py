class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        if N <= 1:
            return N

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        vals = SortedDict()
        vals[A[N - 1]] = N - 1  # Insert the last index

        for i in range(N - 2, -1, -1):
            v = A[i]
            if v in vals:
                odd[i] = even[vals[v]]
                even[i] = odd[vals[v]]
            else:
                lower = vals.peekitem(vals.bisect_left(v) - 1)[0] if vals.bisect_left(v) > 0 else None
                higher = vals.peekitem(vals.bisect_right(v))[0] if vals.bisect_right(v) < len(vals) else None

                if lower is not None:
                    even[i] = odd[vals[lower]]
                if higher is not None:
                    odd[i] = even[vals[higher]]

            vals[v] = i  # Update the SortedDict with the latest index

        return sum(odd)  # Count indices where an odd jump reaches the end
