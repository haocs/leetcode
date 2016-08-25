# source: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(r1, r2): # -> bool
            if not r1 and not r2:
                return True
            if r1 and r2:
                if r1.val == r2.val:
                    return is_mirror(r1.left, r2.right) and is_mirror(r1.right, r2.left)
            return False
        
        if not root:
            return True
        return is_mirror(root.left, root.right)
