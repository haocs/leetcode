# source: https://leetcode.com/problems/triangle/

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = triangle[-1][::]
        for i in range(len(triangle) - 1)[::-1]:
            cur = triangle[i]
            new_list = []
            for idx, num in enumerate(cur):
                new_list.append(num + min(dp[idx], dp[idx+1]))
            dp = new_list
        
        return dp[0]
        
