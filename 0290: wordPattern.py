class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = {}
        checkMap = {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern[i] in wordMap and wordMap[pattern[i]] != words[i]:
                return False
            if words[i] in checkMap and checkMap[words[i]] != pattern[i]:
                return False
            else:
                wordMap[pattern[i]] = words[i]
                checkMap[words[i]] = pattern[i]
        return True