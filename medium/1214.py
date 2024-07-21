""" Two-Sum BSTs """
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        return self.dfs(root1, root2, target)

    def dfs(self, n, t2, k):
        if n is not None:
            d = k - n.val
            if self.bs(t2, d): return True
            if self.dfs(n.left, t2, k): return True
            if self.dfs(n.right, t2, k): return True
        return False

    def bs(self, n, k):
        while n is not None:
            v = n.val
            if k > v: n = n.right
            elif k < v: n = n.left
            else: return True
        return False