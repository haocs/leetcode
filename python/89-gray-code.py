# source: https://leetcode.com/problems/gray-code/

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def get_codes_of_N1_bits(codes, n):
            added = 2 ** (n - 1)
            return codes[::] + [added + k for k in reversed(codes)]
        
        code = [0]
        for i in range(1, n+1):
            code = get_codes_of_N1_bits(code, i)
        return code
