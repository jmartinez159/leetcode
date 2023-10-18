class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = (s.upper()).replace('-','')[::-1]
        ans = ''
        for i in range(0, len(s), k):
            ans += s[i:i+k]+'-'
        return ans[::-1][1:] # reversed and starts at index 1