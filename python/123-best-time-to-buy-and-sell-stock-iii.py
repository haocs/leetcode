# source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days < 2:
            return 0
        buy_1 = -prices[0]
        sell_1 = 0
        buy_2 = -prices[0]
        sell_2 = 0
        for p in prices[1::]:
            print(sell_1)
            print(buy_1)
            buy_2, sell_2 = max(buy_2, sell_1 - p), max(buy_2 + p, sell_2)
            buy_1, sell_1 = max(buy_1, -p), max(sell_1, p + buy_1)
        return sell_2
