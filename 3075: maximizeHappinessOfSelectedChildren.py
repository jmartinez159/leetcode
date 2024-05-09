class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        picked = 0
        happiness.sort()
        while happiness and k > 0:
            curr = happiness.pop()
            if (curr - picked) <= 0:
                return res
            res += curr - picked
            picked += 1
            k -= 1
        return res