class Solution:
    def reverseWords(self, s: str) -> str:
        wordStack = []
        res = ''
        cur = ''
        for x in s:
            if x == ' ' and len(cur) > 0:
                wordStack.append(cur)
                cur = ''
            elif x == ' ':
                continue
            else:
                cur += x
        
        if len(cur) > 0:
            wordStack.append(cur)
        
        while wordStack:
            cur = wordStack.pop()
            if len(wordStack) == 0:
                res += cur
            else:
                res += cur + ' '
        
        return res