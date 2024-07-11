class Solution(object):
    def isSameTree(self, p, q):
        pv, qv = None, None
        if p:
            pv = p.val
        if q:
            qv = q.val
        if pv == qv:
            if not p:
                return True
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)