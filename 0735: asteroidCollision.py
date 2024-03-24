class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        for x in asteroids:
            if x >= 0:
                stack.append(x)
            else:
                while stack:
                    cur = stack.pop()
                    if (cur + x) == 0:
                        x = 0
                        break
                    if cur > abs(x):
                        stack.append(cur)
                        break
                if len(stack) == 0 and x != 0:
                    res.append(x)
        for x in stack:
            res.append(x)
        return res