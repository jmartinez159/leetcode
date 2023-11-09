class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = int((nums[0]-1)*(nums[1]-1))
        return ans