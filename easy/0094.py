class Solution(object):
    def inorderTraversal(self, root):
        l = []
        self.dfs(root, l)
        return l

    def dfs(self, n, l):
        if n is not None:
            self.dfs(n.left, l)
            l.append(n.val)
            self.dfs(n.right, l)