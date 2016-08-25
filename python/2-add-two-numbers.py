# source: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = ListNode(0)
        ptr = result
        p1 = l1
        p2 = l2
        while p1 or p2:
            v1 = 0
            v2 = 0
            if p1:
                v1 = p1.val
                p1 = p1.next
            if p2:
                v2 = p2.val
                p2 = p2.next
            s = v1 + v2 + carry
            carry = s / 10
            ptr.next = ListNode(s % 10)
            ptr = ptr.next
        if carry:
            ptr.next = ListNode(1)
        return result.next
        
