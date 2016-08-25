# source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def backtracing(digits, cur_s, combinations): # -> void
            if len(cur_s) == len(digits):
                combinations.append(cur_s)
            else:
                cur = len(cur_s)
                for c in mapping[int(digits[cur])]:
                    backtracing(digits, cur_s + c, combinations)
        
        
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'] # 0 to 9
        
        if not digits:
            return []
        combinations = []
        backtracing(digits, '', combinations)
        return combinations
