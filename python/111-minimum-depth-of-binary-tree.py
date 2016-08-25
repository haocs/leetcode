# source: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_d = sys.maxint
        if root.left:
            min_d = min(min_d, self.minDepth(root.left))
        if root.right:
            min_d = min(min_d, self.minDepth(root.right))
        return min_d + 1
