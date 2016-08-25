# source: https://leetcode.com/problems/merge-intervals/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        stack = []
        for itv in intervals:
            if not stack or stack[-1].end < itv.start:
                stack.append(itv)
            else:
                prev = stack.pop()
                stack.append(Interval(prev.start, max(prev.end, itv.end)))
        return stack
