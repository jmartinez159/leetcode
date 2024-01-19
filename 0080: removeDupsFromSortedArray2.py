class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freqMap = {}
        for x in nums:
            freqMap[x] = freqMap.get(x, 0) +1
        i = 0
        for x in freqMap.keys():
            if freqMap[x] >= 2:
                nums[i] = x
                i+=1
                nums[i] = x
                i+=1
            else:
                nums[i] = x
                i+=1
        return i