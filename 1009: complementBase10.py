class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = []
        while n > 0:
            if n%2 == 0:
                res.append(1)
            else:
                res.append(0)
            n = int(n/2)
        exp = 0
        ans = 0
        for x in res:
            if x:
                ans += int(math.pow(2, exp))
            exp+=1  
        return ans