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
        low, high = -1, n
        while low+1 != high:
            mid = int((high+low)/2)
            if matrix[i][mid] < target:
                low = mid
            elif matrix[i][mid] > target:
                high = mid
            else:
                return True
        return False