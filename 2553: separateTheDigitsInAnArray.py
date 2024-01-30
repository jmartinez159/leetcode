class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            stack = []
            while x > 0:
                stack.append(x%10)
                x = x//10
            while len(stack) > 0:
                res.append(stack.pop())
        return res