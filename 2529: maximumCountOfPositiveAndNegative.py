class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        # nums[low] < 0 <= nums[high]
        def negCount(nums):
            low, high = -1, len(nums)
            while low+1 != high:
                mid = (low+high)//2
                if nums[mid] < 0:
                    low = mid
                else:
                    high = mid
            return high

        # nums[low] <= 0 < nums[high]
        def posCount(nums):
            low, high = -1, len(nums)
            while low+1 != high:
                mid = (low+high)//2
                if nums[mid] <= 0:
                    low = mid
                else:
                    high = mid
            return len(nums) -high


        positive = posCount(nums)
        negative = negCount(nums)
        return max(positive, negative)