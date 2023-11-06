class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        m = {}
        for x in ranges:
            for y in range(x[0], x[1]+1):
                m[y] = 1
        
        for i in range(left, right+1):
            if(i not in m):
                return False
        return True