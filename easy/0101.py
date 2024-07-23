""" Symmetric Tree """
class Solution(object):
    def isSymmetric(self, root):
        def f(a, b):
            av = a.val if a else None
            bv = b.val if b else None
            if av == bv:
                if av is None: return True
                return f(a.left, b.right) and f(a.right, b.left)
            return False
        return f(root, root)