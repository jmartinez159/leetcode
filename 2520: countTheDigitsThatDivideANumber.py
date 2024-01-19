class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        digits = []
        cur = num
        while cur > 0:
            digits.append(int(cur%10))
            cur = int(cur/10)
        for x in digits:
            if (num%x) == 0:
                res += 1
        return res