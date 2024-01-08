class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for x in range(0,2):
            for y in nums:
                ans.append(y)
        return ans