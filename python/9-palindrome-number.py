# source:https://leetcode.com/problems/palindrome-number

class Solution(object):
    def __init__(self):
        self.INT_MAX = 2147483647
        self.INT_MIN = -2147483648
        
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x > self.INT_MAX or x < self.INT_MIN:
            return False
        res = 0
        origin = x
        while x > 0:
            tmp = x % 10
            res = res * 10 + tmp
            x = x / 10
        return origin == res
