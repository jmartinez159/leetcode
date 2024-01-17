class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        def thinIceValid(x, y):
            while x < y:
                if s[x] == s[y]:
                    x+=1
                    y-=1
                else:
                    return False
            return True
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return thinIceValid(i+1,j) or thinIceValid(i,j-1)
        return True
        