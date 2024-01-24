class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = int((low+high)/2)
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                high = mid -1
            else:
                low = mid +1
        return high