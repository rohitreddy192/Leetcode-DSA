class Solution:
    def maxLength(self, arr):
        mpp = {}
        n = len(arr)
        sum = 0
        mpp[0]=-1
        maxLen = 0
        for i in range(n):
            sum += arr[i]
            if sum not in mpp:
                mpp[sum] = i
            maxLen = max(maxLen, i-mpp[sum])
                
        return maxLen