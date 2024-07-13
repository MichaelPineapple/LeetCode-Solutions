""" Diameter of Binary Tree """
class Solution(object):
    def diameterOfBinaryTree(self, root):
        h, d = self.f(root)
        return d

    def f(self, n):
        if n:
            lh, ld = self.f(n.left)
            rh, rd = self.f(n.right)
            h = max(lh, rh) + 1
            d = max(ld, rd, lh + rh + 2)
            return h, d
        return -1, 0