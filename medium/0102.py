""" Binary Tree Level Order Traversal """
# O(n)?
class Solution(object):
    def levelOrder(self, root):
        o = []
        def f(n, h):
            if not n: return
            if len(o) == h: o.append([])
            o[h].append(n.val)
            f(n.left, h + 1)
            f(n.right, h + 1)
        f(root, 0)
        return o