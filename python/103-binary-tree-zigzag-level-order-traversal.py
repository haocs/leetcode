# source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reverse = False
        result = []
        if not root:
            return []
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
            if reverse:
                values.reverse()
            reverse = not reverse
            result.append(values)
        return result
