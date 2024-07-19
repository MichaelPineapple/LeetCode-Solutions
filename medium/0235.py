""" Lowest Common Ancestor of a Binary Search Tree """
# O(n)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        a, b = sorted([q.val, p.val])
        def f(n):
            v = n.val
            if a <= v <= b: return n
            if b <= v: return f(n.left)
            if a >= v: return f(n.right)
        return f(root)











###################################################################################################

# Solution for regular binary tree (not binary SEARCH tree)
# O(n)
class SolutionA(object):
    def lowestCommonAncestor(self, root, p, q):
        self.o = None
        self.qp = [q, p]
        self.f(root)
        return self.o

    def f(self, n):
        if not n: return False
        l, r = self.f(n.left), self.f(n.right)
        if n in self.qp:
            if l or r: self.o = n
            return True
        if l and r: self.o = n
        return l or r

# Alternative solution for regular binary tree (not binary SEARCH tree)
# O(n)
class SolutionB(object):
    def lowestCommonAncestor(self, root, p, q):
        qp = [p, q]

        def f(n):
            if not n: return False, None
            l, x = f(n.left)
            if x: return True, x
            r, y = f(n.right)
            if y: return True, y
            if n in qp:
                if l or r: return True, n
                return True, None
            if l and r: return True, n
            return (l or r), None

        _, o = f(root)
        return o

# Another alternative solution for regular binary tree (not binary SEARCH tree)
# O(n) but slow
class SolutionC(object):
    def lowestCommonAncestor(self, root, p, q):
        def f(n, a):
            if not n: return False
            if n == a: return [n]
            l, r = f(n.left, a), f(n.right, a)
            o = None
            if l: o = l
            if r: o = r
            if o: o.append(n)
            return o
        pl = f(root, p)[::-1]
        ql = f(root, q)[::-1]
        plj, qlj = len(pl), len(ql)
        j = max(plj, qlj)
        lca = None
        for i in range(j):
            px = pl[i] if i < plj else None
            qx = ql[i] if i < qlj else None
            if px == qx: lca = px
        return lca

