class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap = {}
        for x in magazine:
            charMap[x] = charMap.get(x, 0) +1
        for x in ransomNote:
            if x not in charMap or charMap[x] == 0:
                return False
            charMap[x] -= 1
        return True