class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelStack = []
        ans = ''
        vowels = "aeiouAEIOU"
        for x in s:
            if x in vowels:
                vowelStack.append(x)
        for x in s:
            if x in vowels:
                ans += vowelStack.pop()
            else:
                ans += x
        return ans