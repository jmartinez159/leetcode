class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        numsSet = set()
        for x in nums:
            numsSet.add(x)
        if len(numsSet) <= 2:
            return -1
        numsSet = sorted(numsSet)
        numsSet.pop()
        return numsSet.pop()