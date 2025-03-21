class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        sum = 0

        for i in range(n):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                sum += 1
        

        for j in range(1,m):
            if matrix[0][j]==1:
                dp[0][j] = 1
                sum += 1
        

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    sum += dp[i][j]

        print(dp)
        return sum