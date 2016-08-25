# source: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def recursive_inorder(root):
            if not root:
                return
            recursive_inorder(root.left)
            res.append(root.val)
            recursive_inorder(root.right)
            
        def iter_inorder(root):
            stack = []
            while root:
                if root.left:
                    stack.append(root)
                    root = root.left
                    continue
                res.append(root.val)
                while root.right is None:
                    if not stack:
                        return
                    root = stack.pop()
                    res.append(root.val)
                root = root.right
                    
        
        #recursive_inorder(root)
        iter_inorder(root)
        return res
