class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for x in s:
            m[x] = m.get(x, 0) +1
        
        for x in t:
            if m.get(x) is None:
                return False
            else:
                m[x] = m[x] -1 
        for x in s:
            if m[x] != 0:
                return False
        return True