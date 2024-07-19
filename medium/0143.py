""" Reorder List """
# O(n)
class Solution(object):
    def reorderList(self, head):
        a, n = [], head
        while n:
            a.append(n)
            p = n
            n = n.next
            p.next = None
        n, i, p = len(a)-1, 0, None
        while i <= n//2:
            ai, an = a[i], a[n-i]
            if p: p.next = a[i]
            if ai != an: ai.next = an
            p = an
            i += 1