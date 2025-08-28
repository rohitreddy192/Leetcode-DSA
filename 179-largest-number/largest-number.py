class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strNums = [str(num) for num in nums]

        def compare(n1,n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        strNums = sorted(strNums, key=cmp_to_key(compare))

        return str(int("".join(strNums)))