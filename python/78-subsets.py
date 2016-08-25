# source: https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracing(nums, idx, curset, sets):
            sets.append(curset)
            for i in range(idx, len(nums)):
                new_set = curset[::]
                new_set.append(nums[i])
                backtracing(nums, i + 1, new_set, sets)
        
        sets = []
        backtracing(nums, 0, [], sets)
        return sets
