class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        k = len(height)-1
        while i < k:
            h = 0
            if height[i] > height[k]:
                h = height[k]
                k = k-1
            else:
                h = height[i]
                i = i+1
            cur = h*(k-i+1) # +1 because indexes start at 0
            #current end index - current start index h = lesser of 2 heights
            if cur > ans:
                ans = cur
        return ans
