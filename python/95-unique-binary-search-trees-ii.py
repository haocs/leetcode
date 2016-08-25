# source: https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        DP = [[[None] for x in xrange(0, n+1)] for y in xrange(0, n+1)]
        for row in xrange(n, 0, -1):
            for col in xrange(row, n+1):
                if row == col:
                    DP[row][col] = [TreeNode(row)]
                    continue
                trees = []
                for r in xrange(row, col+1):
                    left_a = DP[row][r - 1]
                    right_a = [None] if r == col else DP[r + 1][col]
                    for i in left_a:
                        for j in right_a:
                            root = TreeNode(r)
                            root.left = i
                            root.right = j
                            trees.append(root)
                DP[row][col] = trees
        return DP[1][n]
