class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightTotal = sum(nums)
        count = 0
        for i in range(len(nums)):
            if count != rightTotal - nums[i]:
                rightTotal -= nums[i]
                count += nums[i]
                continue
            else:
                return i
        return -1