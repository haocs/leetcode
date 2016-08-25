# source: https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        triangle = [[1]]
        for i in range(2, numRows + 1):
            prev = triangle[-1]
            cur = [0] * (len(prev) + 1)
            for idx in range(len(cur)):
                left = prev[idx-1] if idx > 0 else 0
                right = prev[idx] if idx < len(prev) else 0
                cur[idx] = left + right
            triangle.append(cur)
        return triangle
