class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) +1
        maxFreq, res = 0, 0
        for k in freqMap.keys():
            maxFreq = max(maxFreq, freqMap[k])
        for k in freqMap.keys():
            if maxFreq == freqMap[k]:
                res += freqMap[k]
        return res