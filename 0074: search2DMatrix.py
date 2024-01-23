class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < m:
            if matrix[i][n-1] >= target:
                break
            i+=1
        if i == m:
            return False
        low, high = 0, n-1
        while low <= high:
            mid = int((low+high)/2)
            if matrix[i][mid] < target:
                low = mid+1
            elif matrix[i][mid] > target:
                high = mid-1
            else:
                return True
        return False