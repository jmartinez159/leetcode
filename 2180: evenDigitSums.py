class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for x in range(1, num+1):
            cur = x
            r = 0
            while cur > 0:
                r = r + int(cur%10)
                cur = int(cur/10)
            if r%2 == 0:
                ans = ans +1
        return ans