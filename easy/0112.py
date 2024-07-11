class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is not None:
            d, l, r = targetSum - root.val, root.left, root.right
            if l is None and r is None and d == 0:
                return True
            return self.hasPathSum(l, d) or self.hasPathSum(r, d)
        return False