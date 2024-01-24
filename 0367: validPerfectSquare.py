class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num
        while low <= high:
            mid = int((low+high)/2)
            if mid*mid == num:
                return True
            elif mid*mid > num:
                high = mid-1
            else:
                low = mid+1
        return False