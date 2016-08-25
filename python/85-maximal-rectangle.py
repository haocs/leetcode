# source: https://leetcode.com/problems/maximal-rectangle/

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def max_area(heights): # -> int
            area = 0
            indexes = []
            for i in range(len(heights)):
                while indexes and heights[indexes[-1]] > heights[i]:
                    idx = indexes.pop() # not right index
                    h = heights[idx]
                    right_idx = i - 1
                    left_idx = -1 if not indexes else indexes[-1] # idx of first bar shorter than h
                    area = max(area, h * (right_idx - left_idx))
                
                indexes.append(i)
            
            while indexes:
                idx = indexes.pop()
                h = heights[idx]
                right_idx = len(heights) - 1
                left_idx = -1 if not indexes else indexes[-1] # idx of first bar shorter than h
                area = max(area, h * (right_idx - left_idx))
            
            return area
                    
        
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        H = [0] * n
        max_rectangle = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    H[j] += 1
                else:
                    H[j] = 0
            max_rectangle = max(max_rectangle, max_area(H))
        return max_rectangle
