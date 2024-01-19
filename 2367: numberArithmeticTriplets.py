class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        numSet = set(nums)
        for i in range(len(nums)):
            if nums[i] + diff in numSet and nums[i]+diff+diff in numSet:
                ans +=1
        return ans