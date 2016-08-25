# source: https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge_two(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        ptr = head
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                ptr.next = p1
                ptr = ptr.next
                p1 = p1.next
                ptr.next = None
            else:
                ptr.next = p2
                ptr = ptr.next
                p2 = p2.next
                ptr.next = None
        if p1:
            ptr.next = p1
        if p2:
            ptr.next = p2
        return head.next
            
            
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        mid = n // 2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])
        return self.merge_two(l1, l2)
