class Solution(object):
    def findTarget(self, root, k):
        return self.dfs(root, root, k)

    def dfs(self, n, r, k):
        if n is not None:
            d = k - n.val
            if self.bs(r, d, n):
                return True
            if self.dfs(n.left, r, k):
                return True
            if self.dfs(n.right, r, k):
                return True
        return False

    def bs(self, n, k, a):
        if n is not None:
            v = n.val
            if k < v:
                if self.bs(n.left, k, a):
                    return True
            elif k > v:
                if self.bs(n.right, k, a):
                    return True
            elif n != a:
                return True
        return False