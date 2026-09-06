class Solution:
    def getLIS(self, arr):
        from bisect import bisect_left

        n = len(arr)

        # lis[i] = length of LIS starting at i
        lis = [1] * n

        tails = []

        # Calculate LIS length starting from every index
        for i in range(n - 1, -1, -1):
            x = -arr[i]

            pos = bisect_left(tails, x)

            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x

            lis[i] = pos + 1

        length = len(tails)

        # Reconstruct using earliest possible index
        ans = []
        prev_val = float('-inf')
        remaining = length

        for i in range(n):
            if arr[i] > prev_val and lis[i] >= remaining:
                ans.append(arr[i])
                prev_val = arr[i]
                remaining -= 1

                if remaining == 0:
                    break

        return ans