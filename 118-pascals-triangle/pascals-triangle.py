class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                if j == 0 or j==i:
                    tmp.append(1)
                    continue
                
                sumOfVal = res[i-1][j]+res[i-1][j-1]
                tmp.append(sumOfVal)
            
            res.append(tuple(tmp))
        
        return res
