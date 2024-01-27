class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ""
        stack = []
        for x in s:
            if x.isalpha() == False:
                continue
            stack.append(x)
        for x in s:
            if x.isalpha() == False:
                res += x
            else:
                res += stack.pop()
        return res