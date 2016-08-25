# source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        profit = 0
        if days < 2:
            return 0
        for i in range(1, days):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
