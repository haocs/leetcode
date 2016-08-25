# source: https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex+1):
            nr = [0] * (len(row) + 1)
            for idx in range(len(nr)):
                left = row[idx-1] if idx > 0 else 0
                right = row[idx] if idx < len(row) else 0
                nr[idx] = left + right
            row = nr
        return row
