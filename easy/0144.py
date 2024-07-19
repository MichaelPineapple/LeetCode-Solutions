""" Binary Tree Preorder Traversal """
class Solution(object):
    def preorderTraversal(self, root):
        o = []
        def f(n):
            if n:
                o.append(n.val)
                f(n.left)
                f(n.right)
        f(root)
        return o