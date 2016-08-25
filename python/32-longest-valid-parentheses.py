# source: https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        V = [0] * n # longest valid ones end with [i]
        open_num = 0
        
        for i, c in enumerate(s):
            if c == '(':
                open_num += 1
            if c == ')' and open_num > 0:
                # find a match
                V[i] = V[i-1] + 2
                # previou (i - V[i])th may be able to added to V[i]
                # '()(()())' see last ')'. it will connect first pair of parentheses
                if i > V[i]:
                    V[i] += V[i - V[i]]
                open_num -= 1
        return 0 if not V else max(V)
