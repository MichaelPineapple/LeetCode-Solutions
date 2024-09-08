""" Flatten Binary Tree to Linked List """
class Solution(object):
    def flatten(self, root):
        a = []
        def f(n):
            if not n: return
            a.append(n)
            f(n.left), f(n.right)
            n.right, n.left = None, None
        f(root)
        node = root
        for n in a[1:]:
            node.right = n
            node = node.right