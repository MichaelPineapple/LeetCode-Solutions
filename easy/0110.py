""" Balanced Binary Tree """
class Solution(object):
    def isBalanced(self, root):
        return self.f(root) > -1

    def f(self, n):
        if n:
            l = self.f(n.left)
            if l == -1:
                return -1
            r = self.f(n.right)
            if r == -1:
                return -1
            if abs(l-r) > 1:
                return -1
            return max(l, r) + 1
        return 0