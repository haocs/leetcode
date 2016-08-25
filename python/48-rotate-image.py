# source: https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def flip_by_x(matrix):
            n = len(matrix)
            for i in range(int(n/2)):
                matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        
        def flip_by_diagonal(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        flip_by_x(matrix)
        flip_by_diagonal(matrix)
