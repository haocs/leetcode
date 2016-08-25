# source: https://leetcode.com/problems/interleaving-string/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        DP = [[True] * (n2 + 1) for _ in range(n1 + 1)]
        for j in range(1, n2 + 1):
            DP[0][j] = DP[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, n1 + 1):
            DP[i][0] = DP[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                DP[i][j] = (DP[i][j-1] and s2[j-1] == s3[i+j-1]) or (DP[i-1][j] and s1[i-1] == s3[i+j-1])
        return DP[n1][n2]
        """
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[True] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 and j == 0:
                    dp[0][0] = True
                elif j == 0:
                    dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
                elif i == 0:
                    dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
                else:
                    dp[i][j] = (dp[i][j-1] and (s2[j-1] == s3[i+j-1])) or (dp[i-1][j] and (s1[i-1] == s3[i+j-1]))
        print(dp)
        return dp[n1][n2]
