class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x] + nums[y]) == target:
                    ans.append(x)
                    ans.append(y)
                    return ans
            