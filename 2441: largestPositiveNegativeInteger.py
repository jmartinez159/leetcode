class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] == nums[j]:
                i+=1
                j-=1
                continue
            if abs(nums[i]) == nums[j]:
                return nums[j]
            if abs(nums[i]) > nums[j]:
                i+=1
            else:
                j-=1
        return -1