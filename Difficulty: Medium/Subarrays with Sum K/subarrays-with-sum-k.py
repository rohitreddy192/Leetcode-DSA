class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        mpp = {0: 1}
        prefix = 0
        cnt = 0

        for x in arr:
            prefix += x

            if prefix - k in mpp:
                cnt += mpp[prefix - k]

            mpp[prefix] = mpp.get(prefix, 0) + 1

        return cnt