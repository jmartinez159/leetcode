class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        cur = ''
        sameInt = False
        keys = set()
        ans = set()
        for x in word:
            if x >= '0' and x <= '9':
                if not sameInt:
                    sameInt = True
                cur+=x
            else:
                sameInt = False
                if cur != '':
                    keys.add(cur)
                cur = ''
        
        if cur != '':
            keys.add(cur)
        for x in keys:
            ans.add(int(x))
        return len(ans)