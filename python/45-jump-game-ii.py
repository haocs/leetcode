# source: https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        step = 1
        max_can_reach = nums[0]
        i = 1
        while i < n:
            if max_can_reach >= n - 1:
                return step
            next_max = max_can_reach
            while i <= max_can_reach:
                next_max = max(next_max, i + nums[i])
                i += 1
            step += 1
            max_can_reach = next_max
        return step
