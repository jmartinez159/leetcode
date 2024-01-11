class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        freqMap = {}
        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            while (r-l+1) - max(freqMap.values()) > k:
                freqMap[s[l]] -=1
                l+=1
            ans = max(ans, r-l+1)
        return ans