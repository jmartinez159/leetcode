class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        stringSet = set()
        for r in range(len(s)):
            while s[r] in stringSet:
                stringSet.remove(s[l])
                l+=1
            stringSet.add(s[r])
            ans = max(ans, r-l+1)
        return ans        