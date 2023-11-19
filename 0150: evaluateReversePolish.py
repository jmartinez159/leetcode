class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNums = []
        ans = 0
        opStr = '+-*/'
        for t in tokens:
            if opStr.find(t) != -1:
                y = stackNums.pop()
                x = stackNums.pop()
                if t == '+':
                    stackNums.append(x+y)
                if t == '-':
                    stackNums.append(x-y)
                if t == '*':
                    stackNums.append(int(x*y))
                if t == '/':
                    stackNums.append(int(x/y))
            else:
                stackNums.append(int(t))
        return stackNums.pop()