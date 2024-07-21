""" Deepest Leaves Sum """
class Solution(object):
    def deepestLeavesSum(self, root):
        d = self.depth(root)
        l = []
        self.getDeep(root, 1, d, l)
        a = 0
        for x in l:
            a += x
        return a

    def depth(self, n):
        if n:
            l = self.depth(n.left)
            r = self.depth(n.right)
            return max(l, r) + 1
        return 0

    def getDeep(self, n, d, D, l):
        if n:
            if d == D:
                l.append(n.val)
            else:
                dd = d + 1
                self.getDeep(n.left, dd, D, l)
                self.getDeep(n.right, dd, D, l)