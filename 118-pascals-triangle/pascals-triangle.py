class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j]+res[i-1][j-1])
            res.append(tuple(temp))
        return res