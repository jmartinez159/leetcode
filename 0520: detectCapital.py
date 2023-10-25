class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        check = '' + word[0]
        if check.islower():
            return False
        for x in range(1, len(word)):
            check = '' + word[x]
            if check.isupper():
                return False
        return True