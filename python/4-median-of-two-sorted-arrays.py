# source: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        L = len1 + len2
        if L % 2 == 1:
            return self.findHelper(nums1, 0, len1-1, nums2, L/2)
        else:
            return (self.findHelper(nums1, 0, len1-1, nums2, L/2) + self.findHelper(nums1, 0, len1-1, nums2, L/2-1)) / 2.0
        
    def findHelper(self, nums1, left, right, nums2, k):
        if len(nums2) == 0:
            return nums1[k]
        if left > right:
            return self.findHelper(nums2, 0, len(nums2)-1, nums1, k)
        i = (left+right)/2
        j = k - i - 1

        if j < 0:
            if j+1==0 and nums2[j+1] >= nums1[i]:
                return nums1[i]
            return self.findHelper(nums1, left, i-1, nums2, k)
        if j+1 >= len(nums2):
            if j+1 == len(nums2) and nums2[j] <= nums1[i]:
                return nums1[i]
            return self.findHelper(nums1, i+1, right, nums2, k)

        if nums2[j] > nums1[i]:
            return self.findHelper(nums1, i+1, right, nums2, k)
        if nums2[j+1] < nums1[i]:
            return self.findHelper(nums1, left, i-1, nums2, k)
        return nums1[i]
