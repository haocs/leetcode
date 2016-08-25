# source: https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def N_space_recover(self, root):
        def inorder_traverse(root):
            path = []
            parent = []
            cur = root
            while cur:
                if cur.left:
                    parent.append(cur)
                    cur = cur.left
                else:
                    while parent and not cur.right:
                        path.append(cur)
                        cur = parent.pop()
                    path.append(cur)
                    # not cur.right is ok
                    cur = cur.right
            return path
            
        
        path = inorder_traverse(root)
        result = []
        for i in range(len(path) - 1):
            if path[i].val > path[i+1].val:
                result.append(path[i])
                result.append(path[i+1])
        if len(result) == 2:
            result[0].val, result[1].val = result[1].val, result[0].val
        if len(result) == 4:
            result[0].val, result[3].val = result[3].val, result[0].val
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.N_space_recover(root)
