class Solution:
    def scoreOfString(self, s: str) -> int:
        vals = []
        res = 0
        for i in range(len(s)-1):
            vals.append(abs(ord(s[i]) - ord(s[i+1])))
        for i in vals:
            res += i
        return res