class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0 or len(nums) == 1:
            return
        res = [0]*len(nums)
        for i in range(len(nums)):
            index = (k+i)%len(nums)
            res[index] = nums[i]
        for i in range(len(nums)):
            nums[i] = res[i]
        return