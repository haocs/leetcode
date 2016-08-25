# source: https://leetcode.com/problems/largest-rectangle-in-histogram/

# each bar in stack representing the left. if the incoming bar is higher than the ones in stack push it. otherwise pop all bars higher
# thathe incoming one since there will be no chance for them to become larger.
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        height_idx = []
        max_area = 0
        n = len(heights)
        for i, height in enumerate(heights):
            while height_idx and heights[height_idx[-1]] > height:
                idx = height_idx.pop()
                h = heights[idx]
                left = -1 if not height_idx else height_idx[-1]
                max_area = max(max_area, h * (i - left - 1))
            height_idx.append(i)
        
        while height_idx:
            idx = height_idx.pop()
            h = heights[idx]
            left = -1 if not height_idx else height_idx[-1]
            max_area = max(max_area, h * (n - left - 1))
        return max_area
