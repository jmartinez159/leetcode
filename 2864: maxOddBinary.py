class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        m = {}
        m[0] = 0
        m[1] = 0
        for x in s:
            if x == '0':
                m[0] = m[0]+1
            if x == '1':
                m[1] = m[1]+1
        # need one 1 for the end to make the number odd
        ans = ''
        m[1] = m[1]-1
        while m[1] > 0:
            ans += '1'
            m[1] = m[1]-1
        while m[0] > 0:
            ans += '0'
            m[0] = m[0]-1
        ans += '1'
        return ans