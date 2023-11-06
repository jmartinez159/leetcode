class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        strNum = str(num)[::-1]
        check = int(strNum)
        checkStr = str(check)[::-1]
        check = int(checkStr)
        return check == num