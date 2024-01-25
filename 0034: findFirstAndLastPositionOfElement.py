class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # [5, 7, 7,      8, 8, 10]
        #        ^       ^
        #        low     high
        # nums[lo] < target <= nums[hi]

        def firstPosition(nums):
            low, high = -1, len(nums)
            while low+1 != high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid
                else:
                    high = mid
            return high

        # [5, 7, 7, 8, 8,      10]
        #              ^       ^
        #              low     high
        # nums[lo] <= target < nums[hi]

        def lastPosition(nums):
            low, high = -1, len(nums)
            while low+1 != high:
                mid = (low+high)//2
                if nums[mid] <= target:
                    low = mid
                else:
                    high = mid
            return low

        first = firstPosition(nums)
        last = lastPosition(nums)

        if first >= 0 and first < len(nums) and nums[first] == target:
            return [first, last]
        return [-1,-1]