""" Binary Tree Postorder Traversal """
class Solution(object):
    def postorderTraversal(self, root):
        o = []
        def f(n):
            if n is None: return
            f(n.left)
            f(n.right)
            o.append(n.val)
        f(root)
        return o