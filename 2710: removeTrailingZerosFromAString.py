class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = int(num)
        while n > 0 and n%10 == 0:
            n = n//10
        return str(n)