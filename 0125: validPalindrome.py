class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        i = 0
        j = len(s) -1
        while i < j:

            if s[i].isalpha() == False and s[i].isdigit() == False:
                i = i+1
                continue
            if s[j].isalpha() == False and s[j].isdigit() == False:
                j = j-1
                continue
            if s[i] != s[j]:
                return False
            i = i+1
            j = j-1

        return True