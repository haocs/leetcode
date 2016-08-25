# source: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if l == -1 or r == -1:
                return -1
            if abs(l - r) > 1:
                return -1
            return 1 + max(l, r)
            
        return height(root) > -1
