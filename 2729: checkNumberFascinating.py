class Solution:
    def isFascinating(self, n: int) -> bool:
        valid = {}
        numStr = '123456789'
        for x in numStr:
            valid[x] = 0
        checkStr = str(n)+str(n*2)+str(n*3)
        for x in checkStr:
            valid[x] = valid.get(x, 0)+1
        
        for x in numStr:
            if valid.get(x) != 1:
                return False
        return True