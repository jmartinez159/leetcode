class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        right = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                ans = max(ans, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return ans