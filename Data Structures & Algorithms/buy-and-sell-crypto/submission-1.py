class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maximums = [0] * n
        maximums[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            maximums[i] = max(maximums[i + 1], prices[i])

        profit = 0
        for i in range(n - 1):
            curr_profit = maximums[i + 1] - prices[i]
            profit = max(profit, curr_profit)
        
        return profit