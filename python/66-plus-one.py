# source: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1
        while i > -1:
            digits[i] += carry
            if digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
            i -= 1
        if carry:
            digits = [1] + digits
        return digits
