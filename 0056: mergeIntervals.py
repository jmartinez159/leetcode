class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        curr = -1
        for x,y in intervals:
            if x > curr:
                res.append([x,y])
            elif res[len(res)-1][1] > y:
                continue
            else:
                res[len(res)-1][1] = y
            curr = y
        return res