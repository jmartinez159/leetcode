class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqMap = {}
        for x in stones:
            freqMap[x] = freqMap.get(x,0) +1
        res = 0
        for x in jewels:
            if x in freqMap:
                res += freqMap[x]
        return res