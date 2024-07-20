""" Construct Binary Tree From Preorder And Inorder Traversal """
from common.TreeNode import TreeNode

# O(n)
class Solution(object):
    def buildTree(self, preorder, inorder):
        def f(p, i):
            if len(p) < 1: return None
            new = TreeNode(p[0])
            j = i.index(new.val) + 1
            pl, pr = p[1:j], p[j:]
            il, ir = i[:j - 1], i[j:]
            l, r = f(pl, il), f(pr, ir)
            new.left, new.right = l, r
            return new
        return f(preorder, inorder)