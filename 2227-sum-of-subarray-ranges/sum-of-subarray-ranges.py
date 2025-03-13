class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9+7
        def pse(arr):
            psee = [i for i in range(n)]
            st = []
            for i in range(0,n):
                while st and arr[st[-1]]>arr[i]:
                    st.pop()
                psee[i] = -1 if not st else st[-1]
                st.append(i)
            return psee
        def nse(arr):
            nsee = [i for i in range(n)]
            st = []
            for i in range(n-1,-1,-1):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                nsee[i] = n if not st else st[-1]
                st.append(i)
            return nsee

        pse = pse(arr)
        nse = nse(arr)
        cnt = 0
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            cnt = (cnt + (left*right*arr[i]))
        return cnt

    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9+7
        def ple(arr):
            plee = [i for i in range(n)]
            st = []
            for i in range(0,n):
                while st and arr[st[-1]]<=arr[i]:
                    st.pop()
                plee[i] = -1 if not st else st[-1]
                st.append(i)
            return plee
        def nle(arr):
            nlee = [i for i in range(n)]
            st = []
            for i in range(n-1,-1,-1):
                while st and arr[st[-1]]<arr[i]:
                    st.pop()
                nlee[i] = n if not st else st[-1]
                st.append(i)
            return nlee

        ple = ple(arr)
        nle = nle(arr)
        cnt = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            cnt = (cnt + (left*right*arr[i]))
        return cnt
    def subArrayRanges(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        return (self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums))