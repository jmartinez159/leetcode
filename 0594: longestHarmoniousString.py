class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m = OrderedDict()
        ans = 0
        for x in nums:
            m[x] = m.get(x,0) +1
        if len(nums) == 1:
            return 0
        keys = sorted(m.keys())
        for y in range(1,len(keys)):
            cur = 0
            x = y -1
            if keys[x] +1 == keys[y]:
                cur = m[keys[x]] + m[keys[y]]
            if cur > ans:
                ans = cur
        return ans