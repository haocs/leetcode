# source: https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def threeSum(nums, l, r, target):
            sums = []
            for i in range(l, r+1):
                if i == l or nums[i] != nums[i-1]:
                    num = nums[i]
                    for pair in twoSum(nums, i+1, r, target - num):
                        sums.append([num] + pair)
            return sums
                
        def twoSum(nums, l, r, target):
            pairs = []
            while l < r:
                if nums[l] + nums[r] == target:
                    pairs.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return pairs
        
        nums.sort()
        sums = []
        n = len(nums)
        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                num = nums[i]
                for triple in threeSum(nums, i+1, n-1, target-num):
                    sums.append([num] + triple)
        return sums
