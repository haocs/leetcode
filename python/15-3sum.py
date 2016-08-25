# source: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums, l, r, target): # -> pairs
            sums = []
            while l < r:
                if nums[l] + nums[r] == target:
                    sums.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return sums
        
        nums.sort()
        sums = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                num = nums[i]
                for pair in twoSum(nums, i+1, len(nums) - 1, -num):
                    sums.append([num] + pair)
        return sums
