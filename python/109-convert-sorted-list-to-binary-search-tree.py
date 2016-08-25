# source: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        dummy = TreeNode(0)
        dummy.next = head
        prev = dummy
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
            prev = prev.next
        node = TreeNode(s.val)
        prev.next = None
        node.left = self.sortedListToBST(dummy.next)
        node.right = self.sortedListToBST(s.next)
        return node
