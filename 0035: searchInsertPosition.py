class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Looking for boundaries instead of target
        # - how are we splitting the list(boundaries)
        low, high = -1, len(nums)
        while low +1 != high:
            mid = int((low+high)/2)
            if nums[mid] < target:
                low = mid
            else:
                high = mid
        return high
        # nums[low] < target <= nums[high]
        # because of this condition we return high