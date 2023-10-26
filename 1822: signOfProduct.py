class Solution:
    def arraySign(self, nums: List[int]) -> int:
        m = {}
        m[1] = 0
        m[-1] = 0
        for x in nums:
            if x == 0:
                return 0
            elif x > 0:
                m[1] = m[1]+1
            else:
                m[-1] = m[-1]+1
        if (m[-1]%2) == 1:
            return -1
        return 1
        