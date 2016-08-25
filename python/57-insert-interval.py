# source: https://leetcode.com/problems/insert-interval/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        stack = [newInterval]
        cur = None
        for itv in intervals:
            cur = cur if cur else stack.pop()
            if itv.end < cur.start:
                stack.append(itv)
            elif itv.start > cur.end:
                stack.append(cur)
                cur = itv
            else:
                cur = Interval(min(itv.start, cur.start), max(itv.end, cur.end))
        if cur:
            stack.append(cur)
        return stack
