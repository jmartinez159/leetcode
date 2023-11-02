class Solution:
    def romanToInt(self, s: str) -> int:
        m = {}
        m['I'] = 1
        m['V'] = 5
        m['X'] = 10
        m['L'] = 50
        m['C'] = 100
        m['D'] = 500
        m['M'] = 1000
        ans = 0
        for x in range(len(s)):
            cur = m[s[x]]
            if (x+1 < len(s)) and cur < m[s[x+1]]:
                ans -= cur
            else:
                ans += cur
        return ans