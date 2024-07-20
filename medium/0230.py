""" Kth Smallest Element In BST """
# O(n)
class Solution(object):
    def kthSmallest(self, root, k):
        a = []
        def f(n):
            if not n: return
            f(n.left)
            a.append(n.val)
            f(n.right)
        f(root)
        return a[k-1]