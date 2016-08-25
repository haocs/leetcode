# source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days < 2:
            return 0
        lowest_price = prices[0]
        max_p = -lowest_price
        for p in prices[1::]:
            lowest_price = min(lowest_price, p)
            max_p = max(max_p, p - lowest_price)
        return max_p
        
