""" Same Tree """
class Solution(object):
    def isSameTree(self, p, q):
        pv = p.val if p else None
        qv = q.val if q else None
        if pv == qv:
            if not p: return True
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)