""" Maximum Depth of Binary Tree """
# O(n)
class Solution(object):
    def maxDepth(self, root):
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0