class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = -1
        for x in strs:
            cur = 0
            if x.isdigit():
                cur = (int(x))
            else:
                cur = len(x)
            if cur > ans:
                ans = cur
        return ans