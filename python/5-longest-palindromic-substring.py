# source: https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    # N^2 time and N^2 space can be optimized to N space with 1-array if needed.
    def longestPalindrome_DP(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        dp = [[False]*l for i in range(l)]
        max = 1
        start = 0
        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j or i + 2 == j:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    if dp[i-1][j-1] and s[i] == s[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                if dp[i][j] and j - i + 1> max:
                    max = j - i + 1
                    start = i
        return s[start : start + max]
    # N^2 and N space     
    def __init__(self):
        self.maxlen = 0
        self.start = 0
        
    def extendpalindrome(self, str, l, r):
        length = len(str)
        while l >= 0 and r < length and str[l] == str[r]:
            l -= 1
            r += 1
        if r - l - 1 > self.maxlen:
            self.maxlen = r - l - 1
            self.start = l + 1
            
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        for i in xrange(0, len(s)):
            self.extendpalindrome(s, i, i)
            self.extendpalindrome(s, i, i+1)
        return s[self.start : self.start + self.maxlen]
