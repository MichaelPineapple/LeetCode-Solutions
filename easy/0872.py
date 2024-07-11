""" Leaf-Similar Trees """
# Time: O(?)
# Space: O(?)
class Solution(object):
    def leafSimilar(self, root1, root2):
        a1, a2 = [], []
        self.leafSearch(root1, a1)
        self.leafSearch(root2, a2)
        return a1 == a2

    def leafSearch(self, n, a):
        if n:
            l = n.left
            r = n.right
            if l or r:
                self.leafSearch(l, a)
                self.leafSearch(r, a)
            else:
                a.append(n.val)