""" Find All The Lonely Nodes """
class Solution(object):
    def getLonelyNodes(self, root):
        o = []
        def f(n, a):
            if not n: return
            if a: o.append(n.val)
            l, r = n.left, n.right
            x = True if (l is None) ^ (r is None) else False
            f(l, x)
            f(r, x)
        f(root, False)
        return o