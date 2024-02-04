class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = []
        i = 0
        curr = ''
        while i < len(s) and len(words) < k:
            if s[i] == ' ':
                words.append(curr)
                curr = ''
            else:
                curr += s[i]
            i += 1
        if len(curr) > 0:
            words.append(curr)
        res = ''
        for string in words:
            res += ' ' + string
        return res[1:]
