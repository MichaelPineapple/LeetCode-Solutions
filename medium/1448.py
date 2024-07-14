""" Count Good Nodes In Binary Tree """
# O(n) Time
# O(n) Space
class Solution(object):
    def goodNodes(self, root):
        return self.f(root, None)

    def f(self, n, m):
        o = 0
        if n:
            v = n.val
            if v >= m or m is None:
                m = v
                o = 1
            o += self.f(n.left, m) + self.f(n.right, m)
        return o