# source: https://leetcode.com/problems/unique-binary-search-trees/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        here, dp[0~3] == dp[3~6] so I use dp[k] instead of a range to reprensent possible values
        """
        dp = [0 for x in xrange(0, n + 1)]
        dp[0] = 1
        for k in xrange(1, n+1):
            for mid in xrange(0, k):
                dp[k] += dp[mid] * dp[k - ( 1 + mid)]
        return dp[n]
