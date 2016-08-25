# source: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_path(root): # int, int
            if not root:
                return -sys.maxint, -sys.maxint
            max_w = root.val
            l_w, l_wo = max_path(root.left)
            r_w, r_wo = max_path(root.right)
            max_w = max(max_w, max_w + l_w, max_w + r_w)
            max_wo = max(max_w, l_wo, r_wo, root.val + l_w + r_w)
            return max_w, max_wo
        
        if not root:
            return 0
        return max_path(root)[1]
        
