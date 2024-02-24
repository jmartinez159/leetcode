class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        minNum, maxNum = 50001, -50001
        freqMap = {}
        for x in nums:
            freqMap[x] = freqMap.get(x,0) +1
            minNum = min(minNum, x)
            maxNum = max(maxNum, x)
        i = minNum
        while i < maxNum+1:
            if i in freqMap:
                for j in range(freqMap[i]):
                    res.append(i)
            i+=1
        return res