""" Binary Tree Right Side View """
# O(n)?
class Solution(object):
    def rightSideView(self, root):
        o = []
        def f(n, h):
            if not n: return
            if len(o) == h: o.append(n.val)
            f(n.right, h+1)
            f(n.left, h+1)
        f(root, 0)
        return o