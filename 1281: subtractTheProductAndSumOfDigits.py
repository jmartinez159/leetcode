class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        res = 1
        while n > 0:
            digits.append(n%10)
            n = n//10
        for x in digits:
            res = res*x
        return res - sum(digits)