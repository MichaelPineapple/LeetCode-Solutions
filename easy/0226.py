""" Invert Binary Tree """
class Solution(object):
    def invertTree(self, root):
        def f(node):
            if not node: return
            node.left, node.right = node.right, node.left
            f(node.left)
            f(node.right)
        f(root)
        return root