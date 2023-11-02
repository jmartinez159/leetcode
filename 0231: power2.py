class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        temp = 0
        while temp <= n:
            temp = math.pow(2, power)
            if temp == n:
                return True
            power +=1
        return False