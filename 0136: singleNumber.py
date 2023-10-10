
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        m = {}
        for x in nums:
            m[x] = m.get(x, 0) + 1
        for x in nums:
            if m[x] == 1:
                return x
        return 0