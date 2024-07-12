""" Maximize Distance To Closest Person """
# O(n) Time
# O(n) Space
class Solution(object):
    def maxDistToClosest(self, seats):
        n = len(seats)
        ix, jx = n, n
        l = [None] * n
        m = 0
        for i in range(n):
            j = n - i - 1
            if seats[i] > 0:
                ix = 0
            else:
                ix += 1
            if seats[j] > 0:
                jx = 0
            else:
                jx += 1
            piv, pivn = l[i], ix
            if piv:
                pivn = min(pivn, piv)
                m = max(m, pivn)
            l[i] = pivn
            pjv, pjvn = l[j], jx
            if pjv:
                pjvn = min(pjvn, pjv)
                m = max(m, pjvn)
            l[j] = pjvn
        return m