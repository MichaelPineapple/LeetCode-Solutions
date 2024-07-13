""" Validate Binary Search Tree """
class Solution(object):
    def isValidBST(self, root, a=-float('inf'), b=float('inf')):
        return (not root) or ((a < root.val < b) and self.isValidBST(root.left, a, root.val) and self.isValidBST(root.right, root.val, b))