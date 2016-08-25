# source: https://leetcode.com/problems/reverse-integer/

import math

class Solution(object):
    def isOverflow(self, x):
        if math.pow(2, 31) > x and -1 * math.pow(2, 31) <= x:
            return False
        return True
        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPosi = x >= 0
        x = abs(x)
        rev = 0
        while (x > 0):
            # Handle the case: 40000
            rev = rev * 10 + (x % 10)
            x /= 10
            if (self.isOverflow(rev)):
                return 0
        if isPosi is False:
            rev *= -1
            if self.isOverflow(rev):
                return 0
        return rev
