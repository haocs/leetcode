# source: https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s;
        res = ""
        idx = 0
        step = (numRows - 1) * 2
        for i in xrange(0, numRows):
            idx = i
            if (i == 0 or i == numRows-1):
                while (idx < len(s)):
                    res += s[idx]
                    idx += step
            else:
                leap = (numRows - i -1) * 2
                while (idx < len(s)):
                    res += s[idx]
                    idx += leap
                    leap = step - leap
        return res
            
