""" Isomorphic Strings """
# O(n)?
class Solution(object):
    def isIsomorphic(self, s, t):
        A, B, X, Y = {}, {}, 0, 0
        for a, b in zip(s, t):
            if a in A: x = A[a]
            else: x = A[a] = X = X + 1
            if b in B: y = B[b]
            else: y = B[b] = Y = Y + 1
            if x != y: return False
        return True