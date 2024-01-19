class Solution:
    def removeStars(self, s: str) -> str:
        letters = []
        for x in s:
            if x == '*' and len(letters) > 0:
                letters.pop()
            else:
                letters.append(x)
        ans = ""
        for x in letters:
            ans += x
        return ans