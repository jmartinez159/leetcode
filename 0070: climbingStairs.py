class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        x, y = 2,3
        for r in range(4, n+1):
            z = x+y
            x = y
            y = z
        return z