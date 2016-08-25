# source: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isvalid(root, maxv, minv):
            if not root:
                return True
            if not minv < root.val < maxv:
                return False
            return isvalid(root.left, root.val, minv) and isvalid(root.right, maxv, root.val)
        
        return isvalid(root, sys.maxint, -sys.maxint - 1)
