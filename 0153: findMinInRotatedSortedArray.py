class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 5001
        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] < res:
                res = nums[mid]
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid-1
        return res