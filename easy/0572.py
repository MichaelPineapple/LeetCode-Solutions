""" Subtree of Another Tree """
# O(n^2)
class Solution(object):
    def isSubtree(self, root, subRoot):

        def g(t, s):
            tv = t.val if t else None
            sv = s.val if s else None
            if sv == tv:
                if sv is None: return True
                if g(t.left, s.left) and g(t.right, s.right): return True
            return False

        def f(t):
            if g(t, subRoot): return True
            if t is None: return False
            return f(t.left) or f(t.right)

        return f(root)