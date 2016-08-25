# source: https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        scan twice from left to right
        1st. switch if nums[i] - 1 != i and -1 < num[i] < n otherwise, i += 1
        2nd. first i that nums[i] != i + 1 is the num missing.
        """
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if num != i + 1 and 0 < num <= n and nums[num-1] != num:
                swap_idx = num - 1
                nums[i] = nums[swap_idx]
                nums[swap_idx] = num
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
