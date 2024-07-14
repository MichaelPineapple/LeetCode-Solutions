""" Invert Binary Tree """
class Solution(object):
    def invertTree(self, root):
        self.f(root)
        return root

    def f(self, node):
        if node:
            t = node.left
            node.left = node.right
            node.right = t
            self.f(node.left)
            self.f(node.right)