# source: https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(heights)
        if n < 3:
            return 0
        highest_idx = 0
        for i in range(n):
            if heights[i] > heights[highest_idx]:
                highest_idx = i
        # from let to right
        total = 0
        l_h = 0
        for i in range(highest_idx):
            if heights[i] > l_h:
                l_h = heights[i]
            total += l_h - heights[i]
        # from right to left
        r_h = 0
        for i in range(n-1, highest_idx, -1):
            if heights[i] > r_h:
                r_h = heights[i]
            total += r_h - heights[i]
        return total
