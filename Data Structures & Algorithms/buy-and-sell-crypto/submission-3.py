class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        profit = 0

        while j < len(prices):
            if prices[j] > prices[i]:
                diff = prices[j] - prices[i]
                profit = max(profit, diff)
                j += 1
            else:
                i = j
                j = i + 1
        
        return profit
