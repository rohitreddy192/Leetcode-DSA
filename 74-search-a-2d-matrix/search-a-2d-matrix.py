class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        low, high = 0, r*c-1
        while low<=high:
            mid = (low+high)//2
            n_r, n_c = mid // c, mid % c
            if matrix[n_r][n_c] == target:
                return True
            elif matrix[n_r][n_c] < target:
                low = mid+1
            else:
                high = mid-1

        return False