class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opens = []
        invalids = set()
        res = ''
        for i in range(len(s)):
            if s[i] == '(':
                opens.append(i)
            if s[i] == ')':
                if len(opens) > 0:
                    opens.pop()
                else:
                    invalids.add(i)
        
        while len(opens) > 0:
            invalids.add(opens.pop())

        for i in range(len(s)):
            if i in invalids:
                continue
            res += s[i]
        return res