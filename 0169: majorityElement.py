class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = {}
        n = len(nums)
        for x in nums:
            freqMap[x] = freqMap.get(x, 0) +1

        for x in freqMap.keys():
            if freqMap[x] > n//2:
                return x
         