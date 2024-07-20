""" Sum of Left Leaves """
class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.o = 0
        def f(n, L=False):
            l, r = n.left, n.right
            if l: f(l, True)
            if r: f(r)
            if l == r == None and L: self.o += n.val
        f(root)
        return self.o