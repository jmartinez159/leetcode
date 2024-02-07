class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = '13579'
        i = len(num)-1
        while i >= 0:
            if num[i] in odds:
                return num[0:i+1]
            i -= 1
        return ''