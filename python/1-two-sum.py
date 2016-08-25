# source: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        idxDict = {}
        for idx, num in enumerate(nums):
            another = target - num
            if another in idxDict:
                return [idxDict[another], idx]
            idxDict[num] = idx
        return []
