class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for x in s:
            if x == letter:
                count+=1
        return int(count/len(s)*100)