""" Minimum Depth of Binary Tree """
class Solution(object):
    def minDepth(self, root):
        o = self.dfs(root)
        if o is None:
            return 0
        return o

    def dfs(self, n):
        if n:
            l, r = self.dfs(n.left), self.dfs(n.right)
            if l is not None and r is not None:
                return min(l, r) + 1
            else:
                if l is not None:
                    return l + 1
                elif r is not None:
                    return r + 1
                else:
                    return 1
        return None