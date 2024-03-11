class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = set(order)
        freq = {}
        res = ''
        for x in s:
            freq[x] = freq.get(x, 0) +1
        for x in order:
            while x in freq and freq[x] > 0:
                res += x
                freq[x] -=1
        for x in s:
            if x not in chars:
                res += x
        return res