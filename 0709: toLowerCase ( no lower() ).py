class Solution:
    def toLowerCase(self, s: str) -> str:
        upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lwr = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        for i in range(len(s)):
            if s[i] in upr:
                res += lwr[upr.index(s[i])]
            else:
                res += s[i]
        return res