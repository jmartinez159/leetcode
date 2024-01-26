# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = -1, n
        while low+1 != high:
            mid = (low+high)//2
            if isBadVersion(mid) == False:
                low = mid
            else:
                high = mid
        return high