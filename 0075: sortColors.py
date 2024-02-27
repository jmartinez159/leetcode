class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqMap = {0:0, 1:0, 2:0}
        for x in nums:
            freqMap[x] += 1
        cur = 0
        for i in range(0,3):
            while freqMap[i] > 0:
                nums[cur] = i
                freqMap[i] -= 1
                cur += 1