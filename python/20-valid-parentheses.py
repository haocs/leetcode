# source: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                open_p = stack.pop()
                if open_p+c not in ['()', '[]', '{}']:
                    return False
        return not stack
