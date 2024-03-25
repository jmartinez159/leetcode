class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        res = set()
        for x in nums:
            freq[x] = freq.get(x, 0) +1
        for x in nums:
            if freq[x] > 1:
                res.add(x)
        return res