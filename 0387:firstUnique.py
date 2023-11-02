class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for x in s:
            m[x] = m.get(x, 0) +1
        
        for i in range(len(s)):
            x = s[i] 
            if m[x] == 1:
                return i
        return -1 