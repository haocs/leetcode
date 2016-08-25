# source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        que = [root]
        while que:
            tmpq = []
            values = []
            for node in que:
                values.append(node.val)
                if node.left:
                    tmpq.append(node.left)
                if node.right:
                    tmpq.append(node.right)
            que = tmpq
            result.append(values)
        return result[::-1]
