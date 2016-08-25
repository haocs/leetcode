# source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        while root and root.left:
            ptr = root
            prev = None
            while ptr:
                if prev:
                    prev.next = ptr.left
                ptr.left.next = ptr.right
                prev = ptr.right
                ptr = ptr.next
            root = root.left
