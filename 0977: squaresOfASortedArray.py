class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        low, high = 0, len(nums)-1
        while low <= high:
            left, right = abs(nums[low]), abs(nums[high])
            if left > right:
                res[high-low] = left*left
                low += 1
            else:
                res[high-low] = right*right
                high -= 1
        return res